# -*- coding:utf-8 -*-
import urllib
import urllib.request as urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    result = urllib2.urlopen(request)
except urllib2.HTTPError as e:
    if hasattr(e, 'code'):
        print(e.code)
except urllib2.URLError as e:
    if hasattr(e, 'reason'):
        print(e.reason)

content = result.read().decode('utf-8')

pattern_comment = re.compile('<div class="author clearfix">.*?title=.*?<h2>(.*?)</h2>' + 
                             '.*?<div class="content">.*?<span>(.*?)</span>' + 
                             '.*?</a>(.*?)<div class="stats">.*?<i class="number">(.*?)</i>'+
                             '.*?<div class="single-clear"></div>(.*?)</div>', re.S)
items = re.findall(pattern_comment, content)
for item in items:
    haveImg = re.search('class="thumb"', item[2])
    if not haveImg:
        print("author:", item[0])
        story, number = re.subn('<br/>', '\n', item[1]) 
        print("content:")
        print(story)
        print("laughed number:", item[3])
#         print("item4:", item[4])
        pattern_try = re.compile('<span class="cmt-name">(.*?)</span>'+
                                 '.*?<div class="main-text">.(.*?).<div', re.S)
        hasComment = re.findall(pattern_try, item[4])  
        if hasComment:
            for e in hasComment:
                print("Great comment:",e[1],". Author:", e[0])
        print()



