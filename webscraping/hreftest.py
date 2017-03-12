from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bs0bj=BeautifulSoup(html,"lxml")
for link in bs0bj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
