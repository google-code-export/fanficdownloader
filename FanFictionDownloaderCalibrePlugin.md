# Introduction #

Calibre is an very popular ebook management system, written in Python, and extensible by python plugins.

FanFictionDownloader is a tool, written in Python, for downloading fanfiction stories from various web sites and generating consistent ebooks from them.

Bringing the two together with a Calibre plugin is a natural extension of FanFictionDownloader.

# Details #

Hopefully, the hardest part about using the plugin will be getting it setup and on your toolbar.

  1. First, obviously, you need to have [Calibre](http://calibre-ebook.com/) installed and setup.
  1. If you previously installed the Plugin (<1.0.3) manually, you'll need to uninstall it first.  Your preferences will be saved.
  1. You will need to download the plugin.  The latest version is available inside Calibre.  Go to Preferences, Get Plugins, pick FanFictionDownLoader, Install.
  1. You may then be asked which toolbars/menus you would like the plugin to appear on if it is designed to have a user interface.  I suggest adding it to your main toolbar.
  1. Restart Calibre after installing a plugin.
  1. If the FanFictionDownloader button doesn't appear, you may need to go to Preferences->Toolbar and add it.

The official Calibre Introduction to plugins is [here](http://www.mobileread.com/forums/showthread.php?t=118680).

The official distribution point for the plugin is the [forum](http://www.mobileread.com/forums/showthread.php?t=163261) on mobileread.com.

Once installed, the plugin should be very simple to use.

Click the FanFictionDownloader button.  A dialog will open prompting you for URL(s) to download.  As a convenience, the contents of the clipboard will already be copied in.

You can then choose your preferred format, what you want to happen if you already have a copy of that story, and whether the story metadata (title, author, tags, etc) should be updated if it's not a new story.

If you have one or more books selected that the plugin instead try to update them.

The Configuration for this plugin lets you save your defaults for the options above, plus save a 'personal.ini' equivalent.  Perhaps most usefully, the 'personal.ini' section lets you declare you are always 'an adult' and save usernames and passwords for those sites that require them.

We'd love to hear from you at our [user group](http://groups.google.com/group/fanfic-downloader) with any problems or comments you may have.

The latest feature in the plugin is the ability to update lists in the Reading List plugin automatically.  See http://code.google.com/p/fanficdownloader/wiki/FanFictionDownLoaderPluginWithReadingList

# Mac User Crashes #

Some Mac users have had problems with FFDL plugin crashing calibre entirely.  This has been extremely difficult to fix because it only happens for some Mac users.

To work around it, if you are a Mac user, and the FFDL plugin causes calibre to crash for you, you can create a specially named file that FFDL plugin will look for as a flag to disable certain code that seems to cause the crashes.

First, you need to open the Calibre plugin folder.

The Calibre plugin folder is at ~/Library/Preferences/calibre/plugins where ‘~’ is the user’s home folder, which is generally (though not always) called their username, and located at Primary Hard Drive/Users/

Note that in OS X 10.7 and up, users’ Library folders (as distinct from the system Library folder) are hidden. One can get there in Finder by clicking Go > Go to Folder… in the menu bar and entering ~/Library/Preferences/calibre/plugins in the dialogue box. The default keyboard shortcut for Go to Folder is Command + Shift + G
(thanks to seabream for the Mac instructions)

Once there, create a file named fanfictiondownloader\_macmenuhack.txt.

Restart calibre.

This will disable the menu and keyboard shortcuts for FFDL plugin configuration and 'about'.  You can still configure it by drilling down via calibre's preferences > plugins > UI Plugins, search for FanFictionDownloader.