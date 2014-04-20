from bs4 import BeautifulSoup
import urllib2
import requests

#r = requests.get("http://www.npatel.me")

#data = r.text


#an alternate way of getting all of a webpage

response = urllib2.urlopen("http://www.cnn.com/2014/04/19/world/asia/south-korea-ship-sinking/index.html?hpt=hp_t1")

#get a page
page_source = response.read()
soup = BeautifulSoup(page_source)
page = ""

#get a paragraph and then remove all of the tags in it
for para in soup.find_all('p'):
    page += para.getText()

print page
