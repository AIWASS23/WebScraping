import urllib.request
import bs4

# pega o html da pagina
html = urllib.request.urlopen("http://pythonscraping.com/pages/page1.html")
bs = bs4.BeautifulSoup(html.read(), "html.parser")
bs_lxml = bs4.BeautifulSoup(html.read(), "lxml")
bs_html5lib = bs4.BeautifulSoup(html.read(), "html5lib")

print(bs.h1)
print(bs_lxml.h1)
print(bs_html5lib.h1)
print(html.read())
