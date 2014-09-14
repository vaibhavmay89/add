import urllib
import urlparse
import mechanize
import httplib2
from bs4 import BeautifulSoup

import urllib2

url = urllib2.urlopen("http://www.flipkart.com").read()
soup = BeautifulSoup(url)
for line in soup.find_all('a'):
    links = line.get('href')

for link in links: 
    print link 




