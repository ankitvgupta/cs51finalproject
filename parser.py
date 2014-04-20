from bs4 import BeautifulSoup
import urllib2
import requests
from collections import defaultdict
from collections import Counter



#an alternate way of getting all of a webpage
response = urllib2.urlopen("http://www.cnn.com/2014/04/19/world/asia/south-korea-ship-sinking/index.html?hpt=hp_t1")

#reads in info
page_source = response.read()

#turns page into parseable form
soup = BeautifulSoup(page_source)
page_text = ""

#gets text from all of page
for para in soup.find_all('p'):
    page_text += str(para.getText())

print page_text

#creates dictionary with word counts
count = Counter(page_text.split())
standard_dict_count = dict(count)

print count
print standard_dict_count
