from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.stylesheet', 2)
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver = webdriver.Firefox(firefox_profile=firefox_profile)
journal = []
data = []
url = "http://www.sciencedirect.com/science/article/pii/S1359645414005989"
tree = driver.get(url)

author_list = tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')
print(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()"))
#if len(author_list) >=1: 
print ("paper title:" + str(tree.xpath("//h1[@class = 'svTitle']/text()")))
print ("Journal Name: " + str(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()")))
print("authors" + str(tree.xpath('//ul[@class = "authorGroup noCollab"]/li')))
print("\n\nAbstract" + str(tree.xpath("//p[@id='sp0005']")) +"\n\n")
paperTitle = str(tree.xpath("//h1[@class = 'svTitle']/text()"))
journal = str(tree.xpath("//div[@class='title']/a[@cla22ss='cLink']/span/text()"))
authors = tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')
abstract = str(tree.xpath("//p[@id='sp0005']/text()"))
driver.close()
