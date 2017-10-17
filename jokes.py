import os
import urllib2
from bs4 import BeautifulSoup
import random
import json

def getJoke():
	siteList = [{'urlPath' : 'https://crackmeup-api.herokuapp.com/',
		'categories' : ['random', 'blond', 'dark', 'dirty', 'gender', 'gross','walks-into-a-bar'],
		'key' : 'joke'
	}]
	siteIndex = 0
	site = siteList[siteIndex]

	randomCategory = random.randint(0, len(site['categories']) - 1)
	urlPath = site['urlPath'] + site['categories'][randomCategory]
	jokeSite = urllib2.urlopen(urlPath)
	joke = jokeSite.read()
	jsonLoader = json.loads(joke)
	jokeSite.close()
	return jsonLoader[site['key']]

                                    

