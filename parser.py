from bs4 import BeautifulSoup
import urllib2
#import requests
#from collections import defaultdict
from collections import Counter



def combine_dict(dict1, dict2):
	for key in dict1.keys():
		if key not in dict2:
			dict2[key] = dict1[key]
		else:
			dict2[key] += dict1[key]
	return dict2


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

	return combine_dict (standard_dict, orig_dict)
	#print count
	

def build_dict(filename):
	f = open(filename, 'r')
	init_dict = {}
	for line in f:
		init_dict = parse_page(line, init_dict)
	return init_dict


def divide_dict(dic, val):
	for item in dic:
		dic[item] /= float(val)
	return dic


def create_ordering(dic):
	counter = 0
	newdict = {}
	for key in dic.keys():
		newdict[key] = counter
		counter += 1
	return newdict	


liberal_dict = build_dict('liberal.txt')
conservative_dict = build_dict('conservative.txt')

total_lib_words = sum(liberal_dict.values())
total_conservative_words = sum(conservative_dict.values())



unique_lib_words = len(liberal_dict.keys())
unique_conservative_words = len(conservative_dict.keys())

print unique_conservative_words
print unique_lib_words
#print liberal_dict

liberal_freq_dict = divide_dict(liberal_dict, total_lib_words)
conservative_freq_dict = divide_dict(conservative_dict, total_conservative_words)


#print liberal_freq_dict

joint_dict = combine_dict(liberal_dict, conservative_dict)
unique_joint_words = len(joint_dict.keys())

ordering_dict = create_ordering(joint_dict)
print ordering_dict

print unique_joint_words


#dict2 = parse_page("http://www.cnn.com/2014/04/19/world/asia/south-korea-ship-sinking/index.html?hpt=hp_t1", {'and': 1})
#print dict2['and']
#print dict2

#dict3 = parse_page("http://www.cnn.com/2014/04/19/world/asia/south-korea-ship-sinking/index.html?hpt=hp_t1", {}) 
#print dict3["and"]

