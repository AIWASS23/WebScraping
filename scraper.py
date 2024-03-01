import urllib.request
import urllib.error
import bs4

def capturarTitulo(url):
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        return None
    try:
        bs = bs4.BeautifulSoup(html.read(), "html.parser")
        titulo = bs.body.h1
    except AttributeError as e:
        return None
    return titulo

title = capturarTitulo("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("title could not be found")
else:
    print(title)