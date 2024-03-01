import urllib.request
import urllib.error

try:
    #html = urllib.request.urlopen("http://pythonscraping.com/pages/page1.html")
    html_erro = urllib.request.urlopen("http://pythonscrapingthisurldoesnotexist.com")
except urllib.error.HTTPError as erro:
    print("httpErro")
except urllib.error.URLError as urlErro:
    print("urlErro")
else:
    print("Passou")

