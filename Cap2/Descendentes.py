from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html.read(), "html.parser")

for filho in bs.find("table", {"id":"giftList"}).children: # ou usar descendants
    print(filho)