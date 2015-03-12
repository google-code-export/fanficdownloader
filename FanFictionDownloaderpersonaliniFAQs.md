# FanFictionDownloader personal.ini FAQs #

Find a question similar to your query and click on the question - this will take you to an answer.

Do let us have any new questions, or comments about current questions and answers.

For convenience, FanFictionDownloader is abbreviated to FFDL.

#### [General FAQs](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md) ####


---





---


## Can FFDL remember my username and password for different sites? ##
Some sites require login (or login for some rated stories). The program can prompt you, or you can save it in personal.ini.

In the commandline version, this should go in your personal.ini, not defaults.ini.

Code:
```
[www.ficwad.com]
username:YourName
password:yourpassword
```

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)  -  [Comment](FanFictionDownloaderpersonaliniFAQs#Comments.md)

## Guidance on settings for personal.ini ##

For the Calibre FFDL plugin, at the bottom of the personal.ini tab, there's a big button for _View Defaults_.  That shows the defaults (with all the comments).

Guidance for the web service version (which is slightly different) can be found here - [see User Configuration](http://fanfictiondownloader.appspot.com/editconfig)

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)  -  [Comment](FanFictionDownloaderpersonaliniFAQs#Comments.md)

## How can I keep FFDL from asking me if I am an adult all the time? ##
Some sites also require the user to confirm they are adult for adult content.

In the commandline version, this should go in your personal.ini, not defaults.ini.

Code:
```
[defaults]
is_adult:true
```

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)  -  [Comment](FanFictionDownloaderpersonaliniFAQs#Comments.md)

## My settings in personal.ini disappeared after updating the plugin - what happened? ##
Every library in Calibre has its own settings and the FFDL configuration is therefore unique to each library. If you have more than one library, this might be what happened. If you only have one library and you still believe you have _lost_ your FFDL configuration, then do let us know.

> Note: The first time you open the FFDL plugin config in a new library, it will copy the settings from the previously open library - if there was one.

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)

## Why don't my CSS formatting changes in personal.ini work? ##
This is often caused by something very minor. If you still have difficulty after checking the following, then do contact us - see [How do I report problems or ask questions?](FanFictionDownloaderFAQs#How_do_I_report_problems_or_ask_questions.md)

> All CSS style sheets are case-insensitive, except for parts that are not under the control of CSS. For example, the case-sensitivity of values of the HTML attributes 'id' and 'class', of font names, and of URLs lies outside the scope of this specification. Note in particular that element names are case-insensitive in HTML, but case-sensitive in XML. (eg If your CSS uses `<p>` and the story contains `<P>`, then the formatting will not work).

> In CSS2, identifiers (including element names, classes, and IDs in selectors) can contain only the characters [A-Za-z0-9] and ISO 10646 characters 161 and higher, plus the hyphen (-); they cannot start with a hyphen or a digit. They can also contain escaped characters and any ISO 10646 character as a numeric code (see next item). For instance, the identifier 'B&W?' may be written as 'B\&W\?' or 'B\26 W\3F'.

For more information, read http://www.w3.org/TR/REC-CSS2/syndata.html#q4

One common issue is that a story may not be using your CSS at all because you tried to apply everything to `<P>` tags and the story doesn't contain any `<P>` tags at all - all vertical spacing is done with `<BR/>` tags. Applying the formatting  to `<DIV>` instead of `<P>` might help. Some stories always have a `<DIV>` tag around the chapter content. But not all sites do - `<BODY>`is the only tag you're guaranteed will be there for all sites.

Unfortunately, CSS for exact appearance is always going to be an iffy proposition because the HTML entered by different authors varies wildly.

That's why the FFDL strips out so much of it. For example, some stories use SPAN with style attributes for italics. The downloader strips out all the style attributes.

This means you may need to experiment with different settings until you find one that works.

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)  -  [Comment](FanFictionDownloaderpersonaliniFAQs#Comments.md)


---


## Settings ##

### Covers ###
The plugin has an option on the Basic  Configuration tab, _Update Cover when Updating Metadata_. When checked, the Calibre cover image will be updated every time the other Calibre metadata is updated (assuming EPUB). If there is a cover image in the EPUB, it will be used. If not, Calibre will generate the usual _from EPUB format_ type cover, usually showing the title page<br />

**Note:** The include\_images and related options are only available in EPUB and HTML output formats in Plugin and CLI.  Images cannot be included using the Web Service, or in MOBI or TXT.  I recommend you use EPUB output in calibre and convert to get images in other formats.

There are three places cover images can come from.

The first is an explicit cover image from the source site. Today, fimfiction.net is the only one - please let us know (with example URLs) if any of the other sites do.

Second, the downloader can use the first image it finds in the story with this paramter. If keep\_summary\_html is also true (see [Summary](FanFictionDownloaderpersonaliniFAQs#Summary.md)), it can come from the summary.

Code:
```
make_firstimage_cover:true
```

Third, you can set a specific image that will be used if one of the other two isn't found.

Code:
```
[www.adastrafanfic.com:epub]

default_cover_image:file:///C:/Users/username/Desktop/nook/images/icon.png

[www.fictionalley.org:epub]

default_cover_image:http://www.somesite.com/someimage.gif
```

Finally, if you want images inside the EPUB, but never want an image cover, you can use:

Code:
```
never_make_cover:true
```

Note also the option in FFDL's configuration to include images.

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)  -  [Comment](FanFictionDownloaderpersonaliniFAQs#Comments.md)

### Image options ###
All images saved to EPUB are converted to jpeg to save size. Further, you can set what size to scale the images down to fit in. Aspect ratio is preserved and images are never scaled up, only down. You can also have them converted to grayscale for additional (minor) space savings.

**Note:** The include\_images and related options are only available in EPUB output format in Plugin and CLI.  Images cannot be included using the Web Service, or in HTML, MOBI or TXT.  Use EPUB output in calibre and convert to get images in other formats.
There are three places cover images can come from.

Code:
```
image_max_size: 580, 725

grayscale_images: true
```

The default size (580,725--width, height) is for my Nook STR. If people tell me what appropriate sizes are for other book readers, I'll include them in the comments.

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)  -  [Comment](FanFictionDownloaderpersonaliniFAQs#Comments.md)

### Summary ###
This setting allows the summary section in the title page to preserve its HTML from the source site. That way, images in the summary will be included. Summary metadata given to Calibre still has HTML stripped for consistency.

Review the following parameter in your personal.ini .

Under section ` [epub]`, add:

```
keep_summary_html:true
```

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)  -  [Comment](FanFictionDownloaderpersonaliniFAQs#Comments.md)

### Series information ###

This needs to be set up in personal.ini. The following setting has been placed in personal.ini and you just need to remove the # in front of the line.

option collect\_series defaults to true except for www.twilighted.net, www.twiwrite.net and www.thewriterscoffeeshop.com - those sites tend to use 'series' for reading lists instead.<br />

[Back to Questions](FanFictionDownloaderpersonaliniFAQs.md)  -  [Comment](FanFictionDownloaderpersonaliniFAQs#Comments.md)

#### Comments ####
Do let us have any new questions, or comments about current questions and answers at the
[user group](https://groups.google.com/forum/#!forum/fanfic-downloader) or the [MobileRead forum for FanFictionDownLoader calibre plugin](http://www.mobileread.com/forums/showthread.php?t=163261)

(Comments on this page are now disabled because I couldn't reply to peoples' questions.)