from bs4 import BeautifulSoup
import urllib2
import requests

#r = requests.get("http://www.npatel.me")

#data = r.text


#an alternate way of getting all of a webpage
response = urllib2.urlopen("http://www.cnn.com/2014/04/19/world/asia/malaysia-airlines-plane/index.html?hpt=hp_t2")
page_source = response.read()
soup = BeautifulSoup(page_source)

for link in soup.find_all('p'):
    print(link)

