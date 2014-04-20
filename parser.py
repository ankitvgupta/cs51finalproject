from bs4 import BeautifulSoup
import urllib2
import requests

#r = requests.get("http://www.npatel.me")

#data = r.text


#an alternate way of getting all of a webpage
response = urllib2.urlopen("http://google.de")
page_source = response.read()

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))

