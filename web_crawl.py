from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
from urlparse import urlparse
from collections import deque
import global_vars
import checkdoc

starting_url = 'http://www.reuters.com/article/2014/04/30/us-usa-fed-idUSBREA3T03720140430'

def extract_base(url):

  breakdown_url = urlparse(url)
  new_url = breakdown_url.scheme + "://" + breakdown_url.netloc + "/"
  return new_url

def crawler(queue, websites, base):
  #print base
  if len(websites) == 100 or len(queue) == 0:
    return websites 
  link = queue.popleft() 
  try: 
    response = urllib2.urlopen(link)
  except:
    return crawler(queue, websites, base)
  page_source = response.read()
  soup = BeautifulSoup(page_source)
  a_tags = soup.select('a[href^=%s]' % base)
  for i in a_tags:
    if ('href' in dict(i.attrs)):
      if str(i['href']) not in websites:
        queue.append(str(i['href']))
  websites.append(link)
  return crawler(queue, websites, base)

def run_tests():
  links_array = crawler(deque([starting_url]), [], extract_base(starting_url))
  print links_array
  open(global_vars.validator_totest, 'w').close()
  f = open(global_vars.validator_totest, 'w')
  for url in links_array:
    f.write(url + "\n")
  f.close()
  
  global_vars.liberal_file = global_vars.orig_liberal_file
  global_vars.conservative_file = global_vars.orig_conservative_file
  checkdoc.parse_test_cases(global_vars.validator_totest)

run_tests()
