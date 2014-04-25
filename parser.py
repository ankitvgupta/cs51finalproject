from bs4 import BeautifulSoup
import urllib2
#import requests
#from collections import defaultdict
from collections import Counter



# given an input url, returns a dictionary of word frequencies of the relevant parts of its contents
def parse_page(url,orig_dict):
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
	standard_dict = dict(count)

	#change to frequencies
#	for word in standard_dict:
	#	standard_dict[word] /= float(total_num_words)

	#print standard_dict_count	


	#print count
	for key in standard_dict.keys():
		if key not in orig_dict:
			orig_dict[key] = standard_dict[key]
		else:
			orig_dict[key] += standard_dict[key]
	return orig_dict

def build_dict(filename):
	f = open(filename, 'r')
	init_dict = {}
	for line in f:
		init_dict = parse_page(line, init_dict)
	return init_dict

liberal_dict = build_dict('liberal.txt')
conservative_dict = build_dict('conservative.txt')



#dict2 = parse_page("http://www.cnn.com/2014/04/19/world/asia/south-korea-ship-sinking/index.html?hpt=hp_t1", {'and': 1})
#print dict2['and']
#print dict2

#dict3 = parse_page("http://www.cnn.com/2014/04/19/world/asia/south-korea-ship-sinking/index.html?hpt=hp_t1", {}) 
#print dict3["and"]

