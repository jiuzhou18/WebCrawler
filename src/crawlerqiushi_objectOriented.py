import urllib
import urllib.request as urllib2
import re
from pip._vendor.distlib.compat import raw_input

class qiushibaike:
    
    def __init__(self):
        self.pageIndex = 1
        self.baseurl = 'http://www.qiushibaike.com/hot/page/'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.enable = False
        self.stories = []
    
    def getPage(self, pageIndex=1):
        try:
            url = self.baseurl + str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            result = urllib2.urlopen(request)
            content = result.read().decode('utf-8')
            return content    
        except urllib2.HTTPError as e:
            if hasattr(e, 'code'):
                print("Error code:", e.code)
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print("Error reason:", e.reason)
        
    def getPageInfo(self, pageIndex = 1):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print("The page load failed.")
            return None
        pattern_comment = re.compile('<div class="author clearfix">.*?title=.*?<h2>(.*?)</h2>' + 
                             '.*?<div class="content">.*?<span>(.*?)</span>' + 
                             '.*?</a>(.*?)<div class="stats">.*?<i class="number">(.*?)</i>'+
                             '.*?<div class="single-clear"></div>(.*?)</div>', re.S)
        items = re.findall(pattern_comment, pageCode)
        pageStories = []
        for item in items:
            haveImg = re.search('class="thumb"', item[2])
            if not haveImg:
                story = re.sub('<br/>', '\n', item[1])
                pageStories.append([item[0].strip(), story.strip(), item[3], item[4]])
        return pageStories
    
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) <2:
                pageStories = self.getPageInfo(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1
    
    def getOneStory(self, pageStories, page):
        print("page: %d.\n" %page)
        for story in pageStories:
            input = raw_input()
#             self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            print("Author: %s\nContent:\n%s\nLaughed number:%s" %(story[0], story[1], story[2]))
            pattern_try = re.compile('<span class="cmt-name">(.*?)</span>'+
                                 '.*?<div class="main-text">.(.*?).<div', re.S)
            hasComment = re.findall(pattern_try, story[3])
            if hasComment:
                for e in hasComment:
                    print("Great comment",e[1],".\nComment author: ",e[0], end ="")
            print()   


    def start(self):
        print("Loading qiushibaike...\n")
        self.enable = True
        self.loadPage()
        while self.enable:
            self.loadPage()
            if len(self.stories)>0:
                onePage = self.stories[0]
                del self.stories
                self.getOneStory(onePage, self.pageIndex-1)


spider = qiushibaike()
spider.start()