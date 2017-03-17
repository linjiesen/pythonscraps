from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

def getInternalLinks(bs0bj,includeUrl):
    internalLinks=[]
    for link in bs0bj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bs0bj,excludeUrl):
    externalLinks=[]
    for link in bs0bj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(adress):
    addressParts=address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bs0bj=BeautifulSoup(html,"lxml")
    externalLinks=getExternalLinks(bs0bj,splitAddress(startingPage)[0])
    if len(ExternalLinks)==0:
        internalLinks=getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink=getRandomExternalLink("http://oreilly.com")
    print("随机外链是:"+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
