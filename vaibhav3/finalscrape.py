from lxml import html
import requests 

page = requests.get('http://www.sciencedirect.com/science/article/pii/S0921883113002434')
tree = html.fromstring(page.text)


#issue_detail = tree.xpath('//div[@class="txt currentVolumes"]/text()')

#[[journal name, path]] 

names = tree.xpath('//a[@class="authorName"]/text()' )
#data-position = tree.xpath('//li[@class="smh5"]/a/@data-pos')
email = tree.xpath('//a[@class = "auth_mail"]/@href')


print (names,email)
