from bs4 import BeautifulSoup
import urllib2
#import requests
#from collections import defaultdict
from collections import Counter
from stemming.porter2 import stem



# combines the keys and values in two passed in dicts 
def combine_dict(dict1, dict2):
  for key in dict1.keys():
    if key not in dict2:
      dict2[key] = dict1[key]
    else:
      dict2[key] += dict1[key]
  return dict2

def stem_and_count(arr):
  stemmed = {}
  for word in arr:
      temp_word = stem(word)
      if temp_word in stemmed:
        stemmed[temp_word] += 1
      else:
        stemmed[temp_word] = 1
  return stemmed
# given an input url, returns a dictionary of word frequencies of the relevant parts of its contents
def parse_page(url,orig_dict):
  # an alternate way of getting all of a webpage
  #print url
  response = urllib2.urlopen(url)

  # reads in info
  page_source = response.read()

  # turns page into parseable form
  soup = BeautifulSoup(page_source)

  # gets text from all of page
  page_text = ""
  for para in soup.find_all('p'):
      page_text += para.getText()
      #print page_text

  # creates dictionary with word counts
  #count = Counter(page_text.split())
  stemmed_dict = stem_and_count(page_text.split())
  #standard_dict = dict(count)
  #print standard_dict
  # returns the combination of the new and old dict 

  #for key in standard_dict:
  #    standard_dict[key] = stem(standard_dict[key])
  return combine_dict (stemmed_dict, orig_dict)
  
# builds a dict of words and their frequences from a passed in file of urls
def build_dict(filename):
  f = open(filename, 'r')
  init_dict = {}
  for line in f:
    init_dict = parse_page(line, init_dict)
  return init_dict

# divides the values in a dict by a certain value
def divide_dict(dic, val):
  for key in dic.keys():
    dic[key] /= float(val)
  return dic

# creates a new dict with ordered keys from a passed in dict
def create_ordering(dic):
  counter = 0
  newdict = {}
  for key in dic.keys():
    newdict[key] = counter
    counter += 1
  return newdict  

# counts the numbers of line in a file
def line_count(fname):
  f = open(fname, 'r')
  line_count = 0
  for line in f:
    line_count += 1
  return line_count


