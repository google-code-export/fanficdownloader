## A few exceptions for different things for adapters

class FailedToDownload(Exception):
    def __init__(self,error):
        self.error=error

    def __str__(self):
        return self.error

class InvalidStoryURL(Exception):
    def __init__(self,url,domain,example):
        self.url=url
        self.domain=domain
        self.example=example
        
    def __str__(self):
        return "Bad Story URL: (%s) for site: (%s) Example: (%s)" % (self.url, self.domain, self.example)

class FailedToLogin(Exception):
    def __init__(self,url,username):
        self.url=url
        self.username=username
        
    def __str__(self):
        return "Failed to Login for URL: (%s) with username: (%s)" % (self.url, self.username)

class AdultCheckRequired(Exception):
    def __init__(self,url):
        self.url=url
        
    def __str__(self):
        return "Story requires confirmation of adult status: (%s)" % self.url

class StoryDoesNotExist(Exception):
    def __init__(self,url):
        self.url=url
        
    def __str__(self):
        return "Story does not exist: (%s)" % self.url

class UnknownSite(Exception):
    def __init__(self,url,supported_sites_list):
        self.url=url
        self.supported_sites_list=supported_sites_list

    def __str__(self):
        return "Unknown Site(%s).  Supported sites: (%s)" % (self.url, ", ".join(self.supported_sites_list))

