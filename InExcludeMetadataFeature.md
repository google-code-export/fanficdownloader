
```
## Include/Exclude metadata
##
## You can use the include/exclude metadata features to either limit
## the values of particular metadata lists to specific values or to
## exclude specific values.  Further, you can conditionally apply each
## line depending on other metadata, use exact strings or regular
## expressions(regex) to match values, and negate matches.
##
## The settings are:
## include_metadata_pre
## exclude_metadata_pre
## include_metadata_post
## exclude_metadata_post
##
## The form of each line is:
## metakey[,metakey]==exactvalue
## metakey[,metakey]=~regex
## metakey[,metakey]==exactvalue&&conditionalkey==exactcondvalue
## metakey[,metakey]=~regex&&conditionalkey==exactcondvalue
## metakey[,metakey]==exactvalue&&conditionalkey=~condregex
```

Well, I set out to make a simple way to include or exclude metadata
values.  But like most of my projects, it quickly spiraled into
something considerably more complex than I'd first intended.

Let's start with some simple cases first.

'Include' in this case really means 'include ONLY these.'  If a
metadata type has lines in include, only those values will be kept,
all others are discarded.

(Note that the separator is `==`, which is different than in
replace\_metadata.)

```
## in stories from site dramione.org, only use these 4 characters, all
## others will be omitted.  Because only characters are listed, only
## characters will be effected.
[dramione.org]
include_metadata_pre:
 characters==Draco Malfoy
 characters==Hermione Granger
 characters==Harry Potter
 characters==Ron Weasley

## in stories from site www.fimfiction.net, only keep these 2
## characters, all others will be omitted.  And only Comedy and
## Adventure genres will be used--all other genres will be omitted.
## All other metadata will be as usual.
[www.fimfiction.net]
include_metadata_pre:
 characters==Twilight Sparkle
 characters==Rainbow Dash
 genre==Comedy
 genre==Adventure
```

If, on the other hand, you want to keep most values, and want to
exclude only certain values you use `exclude` instead.  (The =~ will
be explained next.)

```
## in stories from site thequidditchpitch.org, exclude warnings 'Minor
## Fluff', AU and anything with 'Contains Spoiler' in it; and the genre
## PWP.  All other values will be kept.
[thequidditchpitch.org]
exclude_metadata_pre:
 warnings==Minor Fluff
 warnings==Alternate Universe
 warnings=~Contains Spoiler
 genre==PWP
```

In both include and exclude, you can use regular expressions(regex)
instead of simple strings by using `=~` for the separator.

```
## in stories from site buffynfaith.net, only include ships with Buffy
## in them, even if spelled with a lower case 'b'.
[buffynfaith.net]
include_metadata_pre:
 ships=~[Bb]uffy

## in stories from site www.fimfiction.net, only use these 2
## characters, all others will be omitted.  All other metadata will be
## as usual.
[www.fimfiction.net]
include_metadata_pre:
 characters=~^(Twilight Sparkle|Rainbow Dash)$

## exclude the Mane Six or Main 6 or variation.
exclude_metadata_pre:
 characters=~(Mane|Main) (Six|6)
```

But what happens when you're using a site that has more than one
category of story and you only want to affect one fandom at a time?
You can use conditionals similar to replace\_metadata.  And in
include/exclude, conditionals can be either exact string(==) or
regex(=~) too.

While an include line for say `characters` without a conditional means
only characters explicitly matched by include lines will be kept, an
include line with a conditional only effects stories that meet the
conditional.

```
## in stories from site archiveofourown.org, when category contains
## 'The Hobbit', only include these three characters.  All other
## stories will continue to have full characters.
[archiveofourown.org]
include_metadata_pre:
 characters==Bilbo&&category==The Hobbit
 characters==Samwise&&category==The Hobbit
 characters==Gandalf&&category==The Hobbit

## still on archiveofourown.org, exclude any character with Bucky in
## it, but only for Marvel, Captain America & Avengers
exclude_metadata_pre:
 characters=~Bucky&&category=~(Marvel|Captain America|Avengers)
```

Note that include is applied first, then exclude.

```
## in stories from site buffynfaith.net, only include ships with Buffy
## in them, even if spelled with a lower case 'b'.
[buffynfaith.net]
include_metadata_pre:
 ships=~[Bb]uffy

## But exclude any Buffy/Dawn.
exclude_metadata_pre:
 ships=~[Bb]uffy/Dawn
```

You may have noticed that all the examples so far ended in `_pre`.
That's because all of these were applied **before** replace\_metadata is
applied.  You can also use include\_metadata\_post and
exclude\_metadata\_post to filter **after** replace\_metadata is applied.

```
[default]
replace_metadata:
 ... tons of code to tweak metadata to your exacting standards
 ... and normalize all the character names juuuust right

## Now make sure that only characters that start with your corrected
## formatting are included.
include_metadata_post:
 characters=~^(Books|Anime|Movies)\.
```

Now one last twist.  In addition to == and =~ to match exact strings
and regex, you can also use != and !~ to **negate** the match.  Much of
what you can do with negated matches can be done by include/exclude,
but some things can't.  Don't go crazy with negated matches--Figuring
out which to use when and why can be quite complicated.

```
[www.fimfiction.net]
## These two on their own are functionally equivalent: exclude
## 'Twilight Sparkle' in characters
include_metadata_pre:
 characters!=Twilight Sparkle

exclude_metadata_pre:
 characters==Twilight Sparkle

## But these two are *not*:

## excludes these two as expected.
exclude_metadata_pre:
 characters==Twilight Sparkle
 characters==Rainbow Dash

## includes all characters because Rainbow Dash matches != Twilight
## Sparkle and Twilight Sparkle matches != Rainbow Dash.  So both
## match an include line and are kept.
include_metadata_pre:
 characters!=Twilight Sparkle
 characters!=Rainbow Dash
```

Realistically, I expect negated matches to be more useful in the
conditionals.

```
[fanfiction.net]
## Exclude Harry Porter, Harry Pearson, etc from other fandoms.
exclude_metadata_pre:
 characters==Harry P.&&category!=Harry Potter
```

And finally, if you need a trailing space in a string or regex, you can use `\s` and
FFDL will convert it to a space.