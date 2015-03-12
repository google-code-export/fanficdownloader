# FanFictionDownloader FAQs #


Find a question similar to your query and click on the question - this will take you to an answer.

Do let us have any new questions, or comments about current questions and answers.

For convenience, FanFictionDownloader is abbreviated to FFDL.

### [Online version FAQs](FanFictionDownloaderOnlineversionFAQs.md) ###

### [Personal.ini FAQs](FanFictionDownloaderpersonaliniFAQs.md) ###


---





> 
---



## Why am I having errors downloading from fanfiction.net? ##
The site fanfiction.net has apparently implemented a throttling system that blocks  requests from users who make too many hits to their servers.  The value of 'too many' is not known, but appears to be around 12-15 downloads in short period of time.

The default value for slow\_down\_sleep\_time for fanfiction.net has been increased and the number of servers requests decreased.  That seems to have helped.

But I still strongly recommend using email notifications for updates rather than using FFDL update to check for new chapters.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## A book I downloaded has images (online) but they are not there in the book ##
The Calibre FFDL plugin can turn on images with the  _Include images in EPUBs_  checkbox in configuration.

Also, there are additional image options which can be set up in personal.ini.

See [configuring personal.ini](FanFictionDownloaderpersonaliniFAQs#Image_options.md) for how to achieve this.

**Note:** The include\_images and related options are only available in EPUB and HTML output formats in Plugin and CLI.  Images cannot be included using the Web Service, or in MOBI or TXT.  I recommend that you use EPUB output in calibre and convert to get images in other formats.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Can FFDL collect Series information? ##
FFDL can collect series information  from sites that support it - many do not make this information available in a way that FFDL can use.

See [configuring personal.ini](FanFictionDownloaderpersonaliniFAQs#Series_information.md) for how to do this.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Can FFDL download a story containing images? ##

Yes. You can choose whether to include the images or not, but only in the CLI and Calibre FFDL plugin versions and only in EPUB and HTML formats.

Review the option in FFDL's configuration to include images. Also there are additional image options which can be set in your personal.ini .

See [configuring personal.ini](FanFictionDownloaderpersonaliniFAQs#covers.md) for these additional parameters.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Can FFDL download and set the downloaded books cover? ##
Yes, but only for EPUB and only in the CLI and Calibre FFDL plugin versions.

There are only a very few sites that have explicit cover images.  For the rest, you can use the include\_images and make\_firstimage\_cover options in personal.ini.  Then, if a story contains an image, FFDL will set that as the book's cover.

Note that FFDL can only use the first image found in a story and this may not always be suitable. For example, in many web sites, the first image is a  feedback button image, so the cover's not going to be real great anyway. It is suggested that the Calibre plugin called [Generate Cover](http://www.mobileread.com/forums/showthread.php?t=124219) can be tried in these cases.

If you don't like the result, then try the _Generate Cover_ plugin to set a different cover.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Can FFDL remember my username and password for different sites? ##
Yes.

Some sites require login (or login for some rated stories). The program can prompt you, or you can save it in personal.ini.

(In the commandline version, this should go in your personal.ini, not defaults.ini.)

See [configuring personal.ini](FanFictionDownloaderpersonaliniFAQs.md) for how to do this.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How can I edit stories after being downloaded? ##
This is largely a matter of personal preference, but the following are some options:

Edit an ePub directly using a program such as Sigil. Minor tweaks can also be done using Calibre's tweak eBook option - for ePub and HTMLZ only.

Use Calibre to convert eBook to RTF format and then edit in your word processor of choice. (TXT is also a conversion option but loses any formatting, and more importantly, loses the link (url) to the story and so is not recommended).

> Important: Make sure that while editing, that you do not remove the link to the story in the story's title. Also, conversion to RTF loses  the Title and Author metadata - these will need to be restored otherwise the next step will not match the revised story and will create a new book in Calibre.

> Copy the modified story back into Calibre (or use Calibre's add books option), delete the original eBook, and convert the newly imported story to your desired eBook format.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How can I keep FFDL from asking me if I am an adult all the time? ##
Some sites also require the user to confirm they are adult for adult content. You can, in your personal.ini, set is\_adult:true and it will assume you are an adult.

In the commandline version, this should go in your personal.ini, not defaults.ini.

See [configuring personal.ini](FanFictionDownloaderpersonaliniFAQs.md) for how to do this.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How do I add a URL to an existing book? ##
FFDL will search inside the existing EPUB for a URL embedded in the book (in the dc: source tag).

Alternately, find the URL for the story, and do an _Add from URL(s)_ with _Update Always_ or _Update Calibre metadata only_. There is a plugin called 'Search The Internet' which is very useful for this. The easiest option is probably to search using Google with this plugin.

FFDL is now able to search for the story (or stories) with the URLs provided, and will match the existing story by title and author and update everything.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How do I backup FFDL settings? ##
For CLI, back up your personal.ini file as you would another file.  For Web Service, copy/paste a copy of your personal settings.  For calibre plugin, FFDL keeps your settings in the calibre library database.

The recommended way to do this is to back up the Calibre library directory.

Details of how to achieve this are given in Calibre's User Guide - http://manual.calibre-ebook.com/faq.html#how-do-i-backup-app

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How do I get the latest version of FFDL? ##
There's now a version of this downloader that runs entirely inside the popular [Calibre](http://calibre-ebook.com) eBook management package as a plugin.

Once you have Calibre installed and running, inside Calibre, you can go to Preferences ->Get plug-ins to enhance Calibre, or go to Preferences->Change Calibre Behaviour->Plug-ins->Load plug-in from file - after first downloading from  [the MobileRead forum for FanFictionDownLoader](http://www.mobileread.com/forums/showthread.php?t=163261).

FYI, anytime there's a new version of a plugin, there's a delay before it shows up on the official list of plugins that Calibre watches. (It's managed manually by kiwidude and Kovid).

Calibre automatically notifies when an updated plugin is available, but this can be manually checked by following the above steps and choosing _Check for updated plugins_.

But you don't have to wait for it even if the _check_ step doesn't show an update. You can go into your User Plugins - don't go _into_ Preferences->Change Calibre Behaviour, but choose 'Get plug-ins' from the Preferences drop down menu - view your Installed plugins, choose FanFictionDownLoader and, even though it says there's no new version, click 'Install'. Restart Calibre and you'll have the latest version.

> Important: _Do not take this option if you have installed FFDL from a download (eg a Beta version) as you will revert to the latest public version_.

The official distribution point for the plugin is the [forum](http://www.mobileread.com/forums/showthread.php?t=163261) on mobileread.com.

The CLI download and details are available from: http://code.google.com/p/fanficdownloader/downloads/list.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How do I report problems or ask questions? ##
If you haven't found an answer here, then there are two ways to do this:

We'd love to hear from you at our [user group](http://groups.google.com/group/fanfic-downloader) with any problems or comments you may have.

If you are technically inclined you can contribute to the [project issue group](http://code.google.com/p/fanficdownloader/issues/list).

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How do I set the font size for a book's Summary/Description in calibre? ##
This is not under FFDL's control, but the Summary (Description) displayed in Calibre can be set as follows:

The general answer is in [Calibre's User Manual](http://manual.calibre-ebook.com/customize.html#overriding-icons-templates-etcetera) Customizing Calibre Overriding icons, templates, etcetera.

> First, find your Calibre config dir by doing Preferences->Change Calibre Behaviour->Advanced->Miscellaneous->Open Calibre configuration directory.  Go into resources, and make a directory named 'templates'.

> Then, copy C:\Program Files (x86)\Calibre2\resources\templates\book\_details.css (or equivalent)  to the templates directory you just made.

You may need to edit the preferences first to unset the read only attribute.

Edit your new book\_details.css file and add the font attribute to the .comment tag:

```
.comment {
font-size: 12px;
}
```

... or whatever size you like.

## How do I update the metadata for an existing book in calibre that wasn't downloaded with FFDL? ##
You need to find the URL of the story (book) and add it to the book's listing in Calibre.

See  [How do I add a URL to an existing book?](FanFictionDownloaderFAQs#How_do_I_add_a_URL_to_an_existing_book.md) for how to do this.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How to control what is sent to the Tags fields in Calibre ##
What metadata gets included in the calibre tags is controlled by the personal.ini option include\_subject\_tags.

> Note that there is an option in FFDL's configuration to keep existing tags (or not) and this should be checked or unchecked as appropriate. This becomes relevant when updating an existing story.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## I get an error saying the address is invalid. What should it be? ##
This often happens because the author's page is selected by mistake. Ensure the story's index page or one of the individual chapter pages is selected.

You can see details of the correct pages to select [here](http://fanfictiondownloader.appspot.com).

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## I installed FFDL but can't see it in Calibre ##
First, try re-starting Calibre.

If FFDL is still not visible, then it is possible the step to choose where to display FFDL was missed, or an option was chosen which doesn't apply.

Go to Preferences->Change Calibre Behaviour->Toolbar and choose the location where you want to see FFDL. Add from the list on the left and then move up or down in the list on the right to set FFDL where desired.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## I love FFDL - how can I support on-going development? ##
FFDL is completely free. The best way you can support is by joining the [discussion group](http://groups.google.com/group/fanfic-downloader) and taking part.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## I used to be able to download from a website but it no longer works ##
Fan fiction websites regularly modify their websites as they try to improve their service. To be fair, it is good that they respond to user requests, and also often will be driven to make changes when the underlying software that hosts their website is changed.

Check the user forum to check if this has already been reported, and then notify us if it hasn't - see [Where do I find the discussion forum for FFDL?](FanFictionDownloaderFAQs#Where_do_I_find_the_discussion_forum_for_FFDL.md).

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Is it possible to automatically accept the 'Proceed with updating your library' dialog in calibre? ##

The 'proceed with updating?' dialog used to be skippable, but that risked corrupting your library DB and that the official way to enforce sequential updates is with that calibre 'proceed with updating?' dialog.

It has to do with limitations of the library DB.  It wasn't designed with concurrent access in mind, so there isn't appropriate locking, transaction support, etc.

Suppose you'd kicked off an FFDL download and at the same moment it finished and was updating the DB, you were also updating the DB from some other plugin or action.  The DB cache can be corrupted in that case.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Is it possible to show the completion status of a downloaded story in calibre? ##
FFDL downloads stories which may be in progress and the status (In Progress or Completed) can be made visible in Calibre.

Metadata 'Status' is included in FFDL. By default, it shows up on the story's title page and is either In-Progress or Completed (or similar according to each website's settings).

FFDL also comes default configured to put In-Progress or Completed on each story as a tag. Assuming, of course, that you have the plugin update metadata.

In Calibre, you can create a custom column of one of the text types or a y/n column, and then configure FFDL to update it automatically from the Custom Columns tag of FFDL config.

In steps:

  1. Go to Calibre Preferences->Change Calibre Behaviour->Add your own columns, and add a column (text type or y/n
  1. You will be prompted to re-start Calibre.
  1. After re-start, check the display and drag the new column to where desired
  1. Open FFDL's configuration and go to 'Custom Columns'  - the new field should be listed. Select a value to populate this field with from the drop down list
  1. Update metadata using FF.

Note that this status can also be displayed on a book's cover if using the [Generate Cover](http://www.mobileread.com/forums/showthread.php?t=124219) plugin.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Is there guidance on settings for the personal.ini (configuration)? ##

See [personal.ini FAQs](FanFictionDownloaderpersonaliniFAQs.md)

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## My settings in personal.ini disappeared after updating the calibre plugin - what happened? ##
Every library in Calibre has its own settings and the FFDL configuration is therefore unique to each library. If you have more than one library, this might be what happened. If you only have one library and you still believe you have lost your FFDL configuration, then do let us know.

> Note: The first time you open the FFDL plugin config in a new library, it will copy the settings from the previously open library - if there was one.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## What are Reading Lists in calibre and how do I use them? ##
The [Reading List](http://www.mobileread.com/forums/showthread.php?t=134856) calibre plugin allows users to keep track of which books they would like to read next, and in which order. You can have multiple lists per library.

The [Reading List](http://www.mobileread.com/forums/showthread.php?t=134856) plugin has also allows you to synchronise list(s) to a device either manually or automatically when it is connected.

You also have the ability to generate lists based on the content of your device. In combination with the ability to apply tags or populate a custom column based on membership in a list, this provides an easy way to keep track of books on your device(s) while they are not connected.

Once you've created Reading Lists for sending to your devices, you can configure FFDL to automatically add new/updated stories to those lists.

Reading Lists can also update custom columns automatically. Using that with a [Metadata Plugboard](FanFictionDownloaderFAQs#What_is_a_Calibre_Metadata_plugboard.md), you can put a notation in the title of new books to read when they're sent to your device.

As a convenience, FFDL offers a menu option to remove stories from the _to read_ lists after you've read them and optionally add _read_ stories to the _send to device_ lists again.

[This is an illustrated example](FanFictionDownLoaderPluginWithReadingList.md) of how it could be used.

Please let us know if you have a better way to do this.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## What is a Calibre Metadata plugboard? ##
Plugboards allow the use of eBook metadata to control how eBooks appear in an ebook reader.

For a detailed explanation, visit the [MobileRead Wiki for Calibre](http://wiki.mobileread.com/wiki/Kindle_and_Calibre_Plugboards).

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## What is `ApplicationError:` 5? ##
This is a rather undifferentiated error that the Web Serice application gives for a variety of reasons. (Undifferentiated means it doesn't distinguish between a number of different issues that cause the error).

This often indicates the application was have problems connecting to the fan fiction website.

FFDL tries several times, with longer waits between attempts, when there's a failure to retrieve story data, but sometimes it still fails. Sometimes, the only answer is to try again later.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Where do I find the discussion forum for FFDL? ##
General discussion group - [FanFictionDownLoader Google Group](http://groups.google.com/group/fanfic-downloader)

Calibre plugin forum - [MobileRead forum for FanFictionDownLoader](http://www.mobileread.com/forums/showthread.php?t=163261)

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Where is the online(Web Service) version of FFDL? ##
http://fanfictiondownloader.appspot.com.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Which fan fiction websites are supported by FFDL? ##
You can see details of which websites are supported [here](FanFictionDownloaderSupportedsites.md).

New sites are regularly investigated and added. If you wish to request a new site then do let us know through the user forum  - see [Where do I find the discussion forum for FFDL?](FanFictionDownloaderFAQs#Where_do_I_find_the_discussion_forum_for_FFDL.md).

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Why do I need to login to Google to use the online (web) version of FFDL? ##
This enables FFDL to store your customised [User Configuration](http://fanfictiondownloader.appspot.com/editconfig).

FFDL will store your retrieved story so that you can then view your personal list of [previously downloaded fanfics](http://fanfictiondownloader.appspot.com/recent).

Note: FFDL does not use your Google login and password. In fact, all FFDL knows about it is your ID - the password is being verified by Google and is absolutely, totally unknown to anyone but you.

Google does not have access to your stored configuration information or details of previously downloaded stories.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Why doesn't FFDL support LiveJournal and many other popular fan fiction websites? ##
Downloading stories from LiveJournal and several other fan fiction websites is potentially possible, but very difficult. Generally, the problem is picking the story out of the rest of the text. Some sites are just too complex - complex layout, embedded comments from readers, etc.

See [Which fan fiction websites are supported by FFDL?](FanFictionDownloaderSupportedsites.md) for more information.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Why has the online version of FFDL stopped working? ##
The service (fanfictiondownloader.appspot.com) has a daily quota and it is likely this has been reached. It will usually start working again after a few hours.

Generally, it is recommended to use the Calibre plugin or command line versions if possible.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Is there a GUI version of FFDL? ##
Right now, the calibre plugin is the only GUI version.

A standalone GUI version isn't on our todo list, but if someone wants to make one, we accept code contributions.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## How can I run the CLI version without installing Python? ##
It's impossible without some sort of Python available, but if you already have calibre installed, you can use it to run the CLI FanFictionDownloader:

`calibre-debug -e downloader.py -- [options to downloader]`

Although, if you have calibre, I'd recommend the FFDL calibre plugin.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Why doesn't the MOBI output show chapters markers on the progress bar in Kindle or include images? ##
FFDL's mobi output is less than ideal--it doesn't include chapter markers, nor can it include images.  These are complex problems because mobi is much more difficult to work with than epub.

Right now, our best suggestion is to download as epub and then convert to mobi.  Using the FFDL calibre plugin and [Reading List](http://www.mobileread.com/forums/showthread.php?t=134856) calibre plugin can make that very easy, if mildly time consuming.  The Web Service includes a link to convertfiles.com, an ebook conversion service, for each finished epub.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

## Why does my Kindle never finish indexing some FFDL books? / Why do some FFDL books break search on my Kindle? ##

Some sites / stories have poor HTML that can cause problems with Kindle's word indexing system.

[This post by Dylan Tomorrow](http://www.mobileread.com/forums/showthread.php?p=2266565&postcount=930) on the FFDL PI forum describes the problem and one solution for it using kindlegen.

## Why doesn't FFDL support other output types, like PDF? ##
Lack of interest by the developers, primarily.  However, if someone comes forward and wants to write the code to add support for new output formats, we'd be happy to work with them.

[Back to Questions](FanFictionDownloaderFAQs#FanFictionDownloader_FAQs.md)  -  [Comment](FanFictionDownloaderFAQs#Comments.md)

### Comments ###
Do let us have any new questions, or comments about current questions and answers at the
[user group](https://groups.google.com/forum/#!forum/fanfic-downloader) or the [MobileRead forum for FanFictionDownLoader calibre plugin](http://www.mobileread.com/forums/showthread.php?t=163261)

(Comments on this page are now disabled because I couldn't reply to peoples' questions.)