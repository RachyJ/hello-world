import urllib.request

try:
    urllib.request.urlopen("http://baidu.com", timeout = 2)
    print("working connection")
except:
    print("No Internet connection")
