import urllib
from http import cookiejar as cookielib

filename = 'cookies.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
account = {
        'email': '******@163.com',
        'password': '111111'
        }
postdata = urllib.parse.urlencode(account).encode('utf-8')
loginUrl = 'http://www.imooc.com/user/newlogin'
infoUrl = 'http://www.imooc.com/u/2855874/courses'
try:
    result = opener.open(loginUrl, postdata)
    cookie.save(ignore_discard=True, ignore_expires=True)
    result = opener.open(infoUrl)
    print(result.read())
except urllib.request.HTTPError as e:
    if hasattr(e, "code"):
        print (e.code)
except urllib.request.URLError as e:
    if hasattr(e, "reason"):
        print (e.reason)