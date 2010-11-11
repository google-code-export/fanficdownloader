# -*- coding: utf-8 -*-

import os
import re
import sys
import shutil
import os.path
import urllib as u
import logging
import pprint as pp
import unittest
import urllib2 as u2
import urlparse as up
import BeautifulSoup as bs
import htmlentitydefs as hdefs
import time
import datetime

from adapter import *
import twipassword

class Twilighted(FanfictionSiteAdapter):
    def __init__(self, url):
        self.url = url
        parsedUrl = up.urlparse(url)
        self.host = parsedUrl.netloc
        self.path = parsedUrl.path
        self.opener = u2.build_opener(u2.HTTPCookieProcessor())
        self.password=twipassword.password
        self.login='sigizmund'
        self.storyDescription = 'Fanfiction Story'
        self.authorId = '0'
        self.authorURL = ''
        self.storyId = '0'
        self.storyPublished = datetime.date(1970, 01, 31)
        self.storyCreated = datetime.datetime.now()
        self.storyUpdated = datetime.date(1970, 01, 31)
        self.languageId = 'en-UK'
        self.language = 'English'
        self.subjects = []
        self.subjects.append ('fanfiction')
        self.subjects.append ('Twilight')
        self.publisher = self.host
        self.numChapters = 0
        self.numWords = 0
        self.genre = 'FanFiction'
        self.category = 'Category'
        self.storyStatus = 'In-Progress'
        self.storyRating = 'PG'
        self.storyUserRating = '0'
        self.storyCharacters = []
        self.storySeries = ''
        
        self.chapurl = False
        ss=self.url.split('?')
        logging.debug('ss=%s' % ss)
        if ss is not None and len(ss) > 1:
            sss = ss[1].replace('&amp;','&').split('&')
            logging.debug('sss=%s' % sss)
            if sss is not None and len(sss) > 0:
                ssss = sss[0].split('=')
                logging.debug('ssss=%s' % ssss)
                if ssss is not None and len(ssss) > 1 and ssss[0] == 'sid':
                    self.storyId = ssss[1]
                if len(sss) > 1:
                    ssss = sss[1].split('=')
                    logging.debug('ssss=%s' % ssss)
                    if ssss is not None and len(ssss) > 1 and ssss[0] == 'chapter':
                        self.chapurl = True

        self.url = 'http://' + self.host + '/' + self.path + '?sid=' + self.storyId
        logging.debug('self.url=%s' % self.url)
        
        self.uuid = 'urn:uuid:' + self.host + '-u.' + self.authorId + '-s.' + self.storyId
        logging.debug('self.uuid=%s' % self.uuid)
    
        logging.debug("Created Twilighted: url=%s" % (self.url))


    def requiresLogin(self, url = None):
        # potionsandsnitches.net doesn't require login.
        if self.host == 'potionsandsnitches.net':
          return False
        else:
          return True

    def performLogin(self, url = None):
        data = {}
    
        data['penname'] = self.login
        data['password'] = self.password
        data['cookiecheck'] = '1'
        data['submit'] = 'Submit'
    
        urlvals = u.urlencode(data)
        loginUrl = 'http://' + self.host + self._getLoginScript()
        logging.debug("Will now login to URL %s" % loginUrl)
    
        req = self.opener.open(loginUrl, urlvals)
    
        d = req.read().decode('utf-8')
    
        if self.reqLoginData(d) :
          return False
        else:
          return True


    def setLogin(self, login):
        self.login = login

    def setPassword(self, password):
        self.password = password

    def _addSubject(self, subject):
        subj = subject.upper()
        for s in self.subjects:
            if s.upper() == subj:
                return False
        self.subjects.append(subject)
        return True

    def _addCharacter(self, character):
        chara = character.upper()
        for c in self.storyCharacters:
            if c.upper() == chara:
                return False
        self.storyCharacters.append(character)
        return True

    def extractIndividualUrls(self):
        url = self.url + '&chapter=1'
        data = self.opener.open(url).read()
        
        if self.reqLoginData(data):
          self.performLogin()
          data = self.opener.open(url).read()
          if self.reqLoginData(data):
            return None
        
        soup = bs.BeautifulStoneSoup(data)

        title = soup.find('title').string
        logging.debug('Title: %s' % title)
        self.storyName = title.split(' by ')[0].strip()
        self.authorName = title.split(' by ')[1].strip()
        self.outputName = self.storyName.replace(" ", "_") + '-tw_' + self.storyId

        logging.debug('self.storyId=%s, self.storyName=%s, self.outputName=%s' % (self.storyId, self.storyName, self.outputName))
        logging.debug('self.authorId=%s, self.authorName=%s' % (self.authorId, self.authorName))
                
        select = soup.find('select', { 'name' : 'chapter' } )
    	 
        result = []
        if select is None:
    	   # no chapters found, try url by itself.
    	   result.append((self.url,self.storyName))
        else:
    	   allOptions = select.findAll('option')
    	   for o in allOptions:
    	     url = self.url + "&chapter=%s" % o['value']
    	     title = o.string
    	     result.append((url,title))
    
        url = self.url + "&index=1"
        data = self.opener.open(url).read()
        lines = data.split('\n')
        soup = bs.BeautifulStoneSoup(data)
        metas = soup.findAll('meta')
        
        for meta in metas:
            if 'name' in meta._getAttrMap() and meta['name'].find('description') != -1:
                #logging.debug('Meta: %s' % meta)
                if 'content' in meta._getAttrMap():
                    s1 = bs.BeautifulStoneSoup(meta['content'])
                    ps = s1.findAll('p')
                    if len(ps) > 0:
                        self.storyDescription = ps[0]
                        logging.debug('self.storyDescription=%s' % (self.storyDescription))
                    else:
                        divs = meta.findAll('div')
                        #logging.debug('Divs: %s' % divs)
                        
                        for div in divs:
                            #logging.debug('Div: %s' % div)
                            if 'id' in div._getAttrMap() and div['id'].find('pagetitle') != -1:
                                #logging.debug('Div PAGETITLE: %s' % div)
                                allA = div.findAll('a')
                                for a in allA:
                                    if 'href' in a._getAttrMap(): 
                                        if a['href'].find('viewstory.php?sid=') != -1:
                                            str1 = a.string
                                            (vs, self.storyId) = a['href'].split('=')
                                            logging.debug('self.storyId=%s self.storyName=%s' % (self.storyId, self.storyName))
                                            self.outputName = self.outputName + "-tw_" + self.storyId
                                            logging.debug('self.outputName=%s' % self.outputName)
                                        if a['href'].find('viewuser.php?uid=') != -1:
                                            str1 = a.string
                                            (vs, self.authorId) = a['href'].split('=')
                                            logging.debug('self.authorId=%s self.authorName=%s' % (self.authorId, self.authorName))
                                            self.authorURL = 'http://'+self.host+'/viewuser.php?uid='+self.authorId
                                            logging.debug('self.authorURL=%s' % self.authorURL)
                            if 'class' in div._getAttrMap() and div['class'].find('content') !=   -1:
                                #logging.debug('Div CONTENT: %s' % div)        
                                brs = div.findAll('br')
                                for br in brs:
                                    buf = unicode(br).encode('utf-8')  
                                    strs = re.split ('<[^>]+>', buf)
                                    #logging.debug('BUF: %s' % strs)
                                    ii = 2
                                    stlen = len(strs)
                                    while stlen > ii+1:
                                        if len(strs[ii]) == 0:
                                            ii = ii+1
                                            continue
                                        if strs[ii] == 'Categories:':
                                            ii = ii+1
                                            while stlen > ii and len(strs[ii]) != 0 and strs[ii].find(':') == -1:
                                                if strs[ii] != ' ' and strs[ii] != ', ':
                                                    if self.category == 'Category':
                                                        self.category = strs[ii].strip(' ')
                                                    self._addSubject(strs[ii].strip(' '))
                                                ii = ii+1
                                            logging.debug('self.subjects=%s' % self.subjects)
                                        if strs[ii] == 'Characters: ':
                                            ii = ii+1
                                            while stlen > ii and len(strs[ii]) != 0 and strs[ii].find(':') == -1:
                                                if strs[ii] != ' ' and strs[ii] != ', ':
                                                    self._addCharacter(strs[ii].strip(' '))
                                                ii = ii+1
                                            logging.debug('self.storyCharacters=%s' % self.storyCharacters)
                                        elif strs[ii] == 'Completed:':
                                            if strs[ii+1].strip(' ') == "No":
                                                self.storyStatus = 'In-Progress'
                                            else:
                                                self.storyStatus = 'Completed'
                                            ii = ii+2
                                            logging.debug('self.storyStatus=%s' % self.storyStatus)
                                        elif strs[ii] == 'Rated:':
                                            self.storyRating = strs[ii+1].strip(' ')
                                            ii = ii+2
                                            logging.debug('self.storyRating=%s' % self.storyRating)
                                        elif strs[ii] == 'Series:':
                                            self.storySeries = strs[ii+1].strip(' ')
                                            if self.storySeries == 'None':
                                                self.storySeries = ''
                                            ii = ii+2
                                            logging.debug('self.storySeries=%s' % self.storySeries)
                                        elif strs[ii] == 'Chapters: ':
                                            self.numChapters = strs[ii+1].strip(' ')
                                            ii = ii+2
                                            logging.debug('self.numChapters=%s' % self.numChapters)
                                        elif strs[ii] == 'Word count:':
                                            self.numWords = strs[ii+1].strip(' ')
                                            ii = ii+2
                                            logging.debug('self.numWords=%s' % self.numWords)
                                        elif strs[ii] == ' Published: ':
                                            self.storyPublished = datetime.datetime.fromtimestamp(time.mktime(time.strptime(strs[ii+1].strip(' '), "%B %d, %Y")))
                                            ii = ii+2
                                            logging.debug('self.storyPublished=%s' % self.storyPublished)
                                        elif strs[ii] == 'Updated:':
                                            self.storyUpdated = datetime.datetime.fromtimestamp(time.mktime(time.strptime(strs[ii+1].strip(' '), "%B %d, %Y")))
                                            ii = ii+2
                                            logging.debug('self.storyUpdated=%s' % self.storyUpdated)
                                        else:
                                            logging.debug('Skipped Label \"%s\" Value \"%s\"' % (strs[ii], strs[ii+1]))
                                            ii = ii+2
                                
        self.uuid = 'urn:uuid:' + self.host + '-u.' + self.authorId + '-s.' + self.storyId
        logging.debug('self.uuid=%s' % self.uuid)

        return result

    def getStoryName(self):
        return self.storyName

    def getOutputName(self):
        return self.outputName
		
    def getAuthorName(self):
        return self.authorName
    
    def getText(self, url):
        if url.find('http://') == -1:
          url = 'http://' + self.host + '/' + url
    
        logging.debug('Getting data from: %s' % url)
    
        data = self.opener.open(url).read()
        
        soup = bs.BeautifulStoneSoup(data, convertEntities=bs.BeautifulStoneSoup.HTML_ENTITIES)
    
        div = soup.find('div', {'id' : 'story'})
    
        if None == div:
          return '<html/>'
    
        return div.__str__('utf8')

    def _getLoginScript(self):
        return '/user.php?action=login'

    def reqLoginData(self, data):
        if data.find('Registered Users Only. Please click OK to login or register.') != -1 or data.find('There is no such account on our website') != -1:
          return True
        else:
          return False

    def getHost(self):
        logging.debug('self.host=%s' % self.host)
        return self.host

    def getStoryURL(self):
        logging.debug('self.url=%s' % self.url)
        return self.url

    def getAuthorURL(self):
        logging.debug('self.authorURL=%s' % self.authorURL)
        return self.authorURL

    def getUUID(self):
        logging.debug('self.uuid=%s' % self.uuid)
        return self.uuid
    
    def getStoryDescription(self):
        logging.debug('self.storyDescription=%s' % self.storyDescription)
        return self.storyDescription
    
    def getStoryPublished(self):
        logging.debug('self.storyPublished=%s' % self.storyPublished)
        return self.storyPublished
    
    def getStoryCreated(self):
        self.storyCreated = datetime.datetime.now()
        logging.debug('self.storyCreated=%s' % self.storyCreated)
        return self.storyCreated
    
    def getStoryUpdated(self):
        logging.debug('self.storyUpdated=%s' % self.storyUpdated)
        return self.storyUpdated
    
    def getLanguage(self):
        logging.debug('self.language=%s' % self.language)
        return self.language
    
    def getLanguageId(self):
        logging.debug('self.languageId=%s' % self.languageId)
        return self.languageId
    
    def getSubjects(self):
        logging.debug('self.subjects=%s' % self.authorName)
        return self.subjects
    
    def getPublisher(self):
        logging.debug('self.publisher=%s' % self.publisher)
        return self.publisher
    
    def getNumChapters(self):
        logging.debug('self.numChapters=%s' % self.numChapters)
        return self.numChapters
    
    def getNumWords(self):
        logging.debug('self.numWords=%s' % self.numWords)
        return self.numWords
    
    def getAuthorId(self):
        logging.debug('self.authorId=%s' % self.authorId)
        return self.authorId
    
    def getStoryId(self):
        logging.debug('self.storyId=%s' % self.storyId)
        return self.storyId
    
    def getCategory(self):
        logging.debug('self.category=%s' % self.category)
        return self.category
    
    def getGenre(self):
        logging.debug('self.genre=%s' % self.genre)
        return self.genre
    
    def getStoryStatus(self):
        logging.debug('self.storyStatus=%s' % self.storyStatus)
        return self.storyStatus
    
    def getStoryRating(self):
        logging.debug('self.storyRating=%s' % self.storyRating)
        return self.storyRating
    
    def getStoryUserRating(self):
        logging.debug('self.storyUserRating=%s' % self.storyUserRating)
        return self.storyUserRating
    
    def getStoryCharacters(self):
        logging.debug('self.storyCharacters=%s' % self.storyCharacters)
        return self.storyCharacters

    def getStorySeries(self):
        logging.debug('self.storySeries=%s' % self.storySeries)
        return self.storySeries

class Twilighted_UnitTests(unittest.TestCase):
  def setUp(self):
    logging.basicConfig(level=logging.DEBUG)
    pass
  
  def testLoginWorks(self):
    url = 'http://www.twilighted.net/viewstory.php?sid=10004'
    self.assertTrue(Twilighted(url).performLogin())
  
  def testGetUrlsWorks(self):
    url = 'http://www.twilighted.net/viewstory.php?sid=10004'
    self.assertEquals(32, len(Twilighted(url).extractIndividualUrls()))

if __name__ == '__main__':
  unittest.main()
