# User Contributed Ideas #
This page is for user-contributed ideas, such as fancy and innovative ways of using Fanfiction Downloader. Leave your comments to this page (they will be visible to everyone) and we'll migrate them to this wiki.

## Testing FFDL Web App ##
It takes rather more setup than using the commandline interface or plugin, but it's possible for users to test and work with the FFDL Web App.

  * **Mercurial(hg)**

You'll need a version of Mercurial(hg) to extract the source.  See:
http://mercurial.selenic.com/downloads/

  * **Google App Engine SDK**

You'll also need Google App Engine SDK, download it from
https://developers.google.com/appengine/downloads and install.  You may need to install Python first if you don't have it already, Python 2.7 is preferred.

  * **FFDL Source**

Get a copy of the full FFDL source using Mercurial(hg).  See:
https://code.google.com/p/fanficdownloader/source/checkout
Anyone can download the source without needing to have update privileges.  You can create a 'clone' of your own if you want, but it's not necessary.

  * **Running Locally**

At this point, you can now use Google App Engine SDK to run the FFDL web service on your local machine.

  * Start 'Google App Engine Launcher'
  * 'Add Existing Application'
  * Choose the directory you downloaded FFDL to.
  * Choose the new application and click 'run'

  * **Running on AppEngine**

Running the app in the SDK is not exactly the same as running it in the cloud.  It's not terribly difficult to run your own instance of the application.

Go to: https://appengine.google.com/
Jump through what ever hoops are necessary to login and get permission to create an application.  Then create an application with your own unique application name.

Edit app.yaml in the FFDL source directory, change 'application' from fanfictiondownloader to your own unique application name from above.  (Change 'version' or not, as you like.)

Then use Google App Engine SDK to deploy the application.