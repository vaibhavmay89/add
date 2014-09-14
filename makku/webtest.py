from lxml import html
import requests 
page = requests.get('http://www.flipkart.com/mobiles/~new-releases/pr?sid=tyy%2C4io&otracker=ch_vn_mobile_main_New%20Arrivals%20in%20Mobile%20Phones_View_All')
tree = html.fromstring(page.text)

buyers = tree.xpath('//a[@class="fk-display-block"]/text()')
prices = tree.xpath('//span[@class="fk-font-17 fk-bold"]/text()')
for i in range (0, len(buyers)):
	buyers[i] = buyers[i].strip(' \n')
	p = ''
	t = len(buyers[i])
	for j in range(0,60-t):
		p += '_' 
		


	print buyers[i]+ p + prices[i]
