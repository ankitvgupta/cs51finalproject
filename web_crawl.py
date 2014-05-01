from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
from urlparse import urlparse
from collections import deque



url = 'http://www.cnn.com/2014/04/29/politics/shumlin-midterms/index.html?hpt=po_c1'

breakdown_url = urlparse(url)
new_url = breakdown_url.scheme + "://" + breakdown_url.netloc

def crawler(queue, websites):
  if len(websites) == 100:
    return websites 
  link = queue.popleft() 
  try: 
    response = urllib2.urlopen(link)
  except:
    return crawler(queue, websites)
  page_source = response.read()
  soup = BeautifulSoup(page_source)
  a_tags = soup.select('a[href^=new_url]')
  for i in a_tags:
    if ('href' in dict(i.attrs)):
      if str(i['href']) not in websites:
        queue.append(str(i['href']))
  websites.append(link)
  return crawler(queue, websites)

print crawler(deque([url]), [])










