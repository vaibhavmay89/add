from lxml import html

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


print '\n\n\n\n\n'
page = urlopen('http://www.sciencedirect.com/science/article/pii/S1359835X14001997')

print '\n\n\n\n\n'
tree = html.fromstring(page.text)



authors = []
#[[journal name, path]] 

names = tree.xpath('//ul[@class="authorGroup noCollab"]/li[class="smh5"]/a[class="authorName"]/text()' )
#data-position = tree.xpath('//ul[@class="authorGroup noCollab"]/li[class="smh5"]/a/@data-pos')
email = tree.xpath('//ul[@class="authorGroup noCollab"]/li[class="smh5"]/a[class = "auth_mail"]/@href')

print names 
print '--------------------------------------'
print data-position
print '--------------------------------------'
print email 