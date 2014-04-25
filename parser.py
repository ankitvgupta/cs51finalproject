from bs4 import BeautifulSoup
import urllib2
#import requests
#from collections import defaultdict
from collections import Counter


# given an input url, returns a dictionary of word frequencies of the relevant parts of its contents
def parse_page(url):
	#an alternate way of getting all of a webpage
	response = urllib2.urlopen(url)

	#reads in info
	page_source = response.read()

	#turns page into parseable form
	soup = BeautifulSoup(page_source)

	#gets text from all of page
	page_text = ""
	for para in soup.find_all('p'):
	    page_text += str(para.getText())

	#print page_text

	#creates dictionary with word counts
	count = Counter(page_text.split())
	standard_dict_count = dict(count)
	total_num_words = sum(standard_dict_count.values())

	#change to frequencies
	for word in standard_dict_count:
		standard_dict_count[word] /= float(total_num_words)

	#print standard_dict_count	


	#print count
	return standard_dict_count

print parse_page("http://www.cnn.com/2014/04/19/world/asia/south-korea-ship-sinking/index.html?hpt=hp_t1")