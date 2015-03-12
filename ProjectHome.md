# FanFictionDownLoader #

FanFictionDownLoader is a tool for downloading fanfiction and original
stories from various sites into ebook form.

## Main Features of FanFictionDownLoader: ##

### Download fanfiction stories from various sites into ebooks. ###

See FanFictionDownloaderSupportedsites for the list of supported sites.

### Create various ebook formats. ###
Currently supported formats are:
  * epub (the preferred open standard used by most readers, including Sony Reader, Nook and iPad )
  * mobi (Kindle)
  * html
  * txt

## Command Line Interface (CLI) version ##

The latest CLI version can be found in the [download area](http://code.google.com/p/fanficdownloader/downloads/list) of this project.  It requires Python 2.5+ to run. (It hasn't been tested with Python 3.)

### Additional features of the CLI ###

  * Can be configured to not overwrite files newer than the last story update.
  * Update existing epub format ebooks, downloading only new chapters.

## Web service version ##

A web service version, powered by Google's AppEngine, can be found
here: http://fanfictiondownloader.appspot.com/

Most, but not all of the same features and options are available in the web version.

### Additional features of the web service ###

  * Retains recent downloads for a day making it easy to start a download from PC and retrieve it on iPad, for example.

## calibre plugin version ##

The calibre plugin version is the most featured version.  It can be
obtained from within calibre itself, or in the Mobile Read
[FanFictionDownLoader plugin forum](http://www.mobileread.com/forums/showthread.php?t=163261).

### Additional features of the calibre plugin ###

  * Runs within calibre on Windows, Mac and Linux.
  * Download in the background for user convenience.
  * Update/Overwrite existing fanfiction stories from story URL in calibre identity field or epub.
  * Update calibre metadata from website.
  * Option to delete other formats on book update.  Handy if you have both a Nook(epub) and Kindle(mobi), for example.
  * Get original URLs from fanfiction stories in your library.
  * Update [Reading List](http://www.mobileread.com/forums/showthread.php?t=134856) plugin lists as an aid to device sync and keeping a list of new books to read.  Requires Reading List plugin 1.4.1 or newer to use.  See FanFictionDownLoaderPluginWithReadingList.
  * Update calibre custom columns with story metadata.