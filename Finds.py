from urllib.request import urlopen
from bs4 import BeautifulSoup

# pega o html da pagina

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html.parser")

nameList = bs.findAll("span", {"class":"green"})
nameTags = bs.find_all(["h1","h2","h3","h4","h5","h6"])
nameAttributes = bs.find_all("span", {"class":{"green", "red"}})
nameTexts = bs.find_all(text = "the prince")
nameKeywords = bs.find_all(id = "title")

for name in nameList: # testar as outras variaveis
    print(name.get_text())

