from bs4 import BeautifulSoup
import urllib2
import requests

response = urllib2.urlopen("http://www.cnn.com/2014/04/19/world/asia/south-korea-ship-sinking/index.html?hpt=hp_t1")

page_source = response.read()

soup = BeautifulSoup(page_source)

page = ""

for para in soup.find_all('p'):
    page += para.getText()

print page
