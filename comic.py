import os
import urllib2
import urllib
from bs4 import BeautifulSoup

def getComic():
    siteList = [{'urlPath': 'http://explosm.net/comics/random',
                  'id': 'main-comic',
                  'srcAppendPath': 'http:'}]
    siteIndex = 0
    site = siteList[siteIndex]


    randomComicPage = urllib2.urlopen(site['urlPath'])
    soup = BeautifulSoup(randomComicPage.read(),'html.parser')

    mainComic = soup.find(id=site['id'])
    print mainComic.get('src')
    imageOpener = urllib.URLopener()
    imageOpener.retrieve(site['srcAppendPath'] + mainComic.get('src'), 'img.png')

