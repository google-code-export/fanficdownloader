#Using FanFictionDownLoader plugin(1.2.0+) with the Reading List plugin to easily manage reading fanfic with a device.

# Introduction #

This is an illustrated example of how I thought the latest version(1.2.0) of the FanFictionDownLoader plugin could be used with the Reading List plugin to easily manage reading fanfic with a device (shown here as a Nook STR).  I assume you already have FanFictionDownLoader and Reading List installed.

# Details #

First, there's a bit of set up.

## Set up a Yes/No custom column to show when book is on the Nook: ##
![http://i.imgur.com/cPXBY.png](http://i.imgur.com/cPXBY.png)


## A second custom column is used to show which books are new.  This will also be used below to flag new books on your ebook reader. ##
![http://i.imgur.com/5WxXJ.png](http://i.imgur.com/5WxXJ.png)


## Before Reading List can sync your device, it has to know about it.  Plug your device in, wait for calibre to recognize it, then go into Reading List config Devices and add it. ##
![http://i.imgur.com/ksG2W.png](http://i.imgur.com/ksG2W.png)


## There will be two lists set up, the first is used to send new/updated books to your device.  Note especially that you want Add/Overwrite. ##
![http://i.imgur.com/t5fkc.png](http://i.imgur.com/t5fkc.png)


## The second list primarily updates the New column. ##
![http://i.imgur.com/v1AS6.png](http://i.imgur.com/v1AS6.png)


## Next is to setup a Metadata plugboard to automatically prepend '000 ' to the book title as it's being copied to the device. ##
![http://i.imgur.com/zGIFo.png](http://i.imgur.com/zGIFo.png)


## Now you go into the FanFictionDownLoader configuration and tell it about the lists you've created. ##
![http://i.imgur.com/bo8eD.png](http://i.imgur.com/bo8eD.png)


## Now when you download a new story (or update an existing one)... ##
![http://i.imgur.com/12UCW.png](http://i.imgur.com/12UCW.png)


## It automatically shows up as New and not yet on the Nook. ##
![http://i.imgur.com/pDEh2.png](http://i.imgur.com/pDEh2.png)


## If you already have your device plugged in, you can sync it immediately from the Reading List menu. ##
![http://i.imgur.com/Nch1U.png](http://i.imgur.com/Nch1U.png)


## After syncing, the book is on the device, but still New. ##
![http://i.imgur.com/xVWi5.png](http://i.imgur.com/xVWi5.png)


## While calibre remembers the real title, the epub(or mobi for Kindle) written to the device has 000 in front thanks to the Metadata plugboard. ##
![http://i.imgur.com/1a0Xg.png](http://i.imgur.com/1a0Xg.png)


## Here it is on the Nook itself, showing up nicely at the top of the titles list. ##
![http://i.imgur.com/ZCREQ.png](http://i.imgur.com/ZCREQ.png)


## After you've read it, you go back and use FanFictionDownLoader again to mark it read.  That will change the New column and put it back on the list to sync to the device.  It has to be written to the device again to replace the version with 000 with a version without. ##
![http://i.imgur.com/HKqKr.png](http://i.imgur.com/HKqKr.png)


## Note now it's read, but needs to be synced again. ##
![http://i.imgur.com/2NafV.png](http://i.imgur.com/2NafV.png)


## If you turned on 'Sync to this device as soon as it is connected' in Reading List, the next time you plug in your device, it will be updated automatically. ##
![http://i.imgur.com/Td9Lt.png](http://i.imgur.com/Td9Lt.png)