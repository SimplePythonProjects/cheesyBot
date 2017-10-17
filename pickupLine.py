import os
import urllib2
from bs4 import BeautifulSoup

def getPickupLine():
    siteList = [{'urlPath' : 'http://www.pickuplinegen.com/',
                 'id' : 'content'}]
    siteIndex = 0
    site = siteList[siteIndex]


    pickupPage = urllib2.urlopen(site['urlPath'])
    soup = BeautifulSoup(pickupPage.read(), 'html.parser')

    pickupLine = soup.find(id=site['id']).text
    return pickupLine
        

