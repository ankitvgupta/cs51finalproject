from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
from urlparse import urlparse



url = 'http://www.cnn.com/2014/04/29/politics/shumlin-midterms/index.html?hpt=po_c1'
response = urllib2.urlopen(url)

  # reads in info
page_source = response.read()

  # turns page into parseable form
soup = BeautifulSoup(page_source)
print soup

links = soup.select('a[href^="http://www.cnn.com/"]')
newlist = []
for i in links:
	if ('href' in dict(i.attrs)):
		print i['href']
	#print links
	newlist.append(urlparse(str(i['href'])))

print newlist



