import urllib.request as urllib2


request = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError as e:
    if hasattr(e, "code"):
        print (e.code)
except urllib2.URLError as e:
    if hasattr(e, "reason"):
        print (e.reason)
else:
    print("OK")
    print (response.read())    


