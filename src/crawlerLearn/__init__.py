import urllib.request as urllib2

response = urllib2.urlopen("http://www.baidu.com")
print (response.read())
