from web_crawl import extract_base,crawler
from parser import parse_page
from collections import deque
from bs4 import BeautifulSoup
from urlparse import urljoin
from urlparse import urlparse
from collections import deque

#takes in article
start_url = 'http://www.cato.org/publications/policy-analysis/how-states-talk-back-washington-strengthen-american-federalism'


#generates list of crawled urls
list_of_articles = crawler(deque([start_url]),[],extract_base(start_url))
print 5
print list_of_articles

#generate dictionary of all words
def dict_gen(articles):
    start_dict = {}
    for article in articles:
        start_dict = parse_page(article,start_dict)
        print start_dict
    return start_dict








