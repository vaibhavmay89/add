from lxml import html
import requests 
import time 
import csv

reqn = 0 
missedlist = []
def writefile(filename,text):
	file = open(filename,"a")
	file.write("\n")
	try:
		file.write(text)
	except:
		printer("UNABLE TO WRITE !")
		file.write("-------- MISSED SOMETHING HERE !! ---------------------------")
		file.close()
		pass


def printer(string):
	print(string)
	writefile("logsSelNR.txt",string)

def openurl(url): 
	global reqn
	time.sleep(2)
	reqn +=1
	printer (str(reqn) + " Requests made so far!")
	page = requests.get(str(url))
	printer (str(reqn) + " Requests made so far!" + str(page.status_code))
	#page = requests.get('https://dl.dropboxusercontent.com/u/7333305/test.html')
	tree = html.fromstring(page.text)
	return tree

data = []
file = open('data.txt','r')
lines = file.readlines()
print(type(lines))
for line in lines:
	line.replace('\n','')
	data.append(line)

list1= []

url = 'http://www.sciencedirect.com/science/article/pii/S1359645414005989?np=y'
for di in range(0,len(data)):
        tree = 0
        p = data[di].replace("\n","")
        p = p.strip()
        print(p)
        tree = openurl(data[di])
        author_list = tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')
        print(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()"))
        #if len(author_list) >=1: 
        print ("paper title:" + str(tree.xpath("//h1[@class = 'svTitle']/text()")))
        print ("Journal Name: " + str(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()")))
        print("authors" + str(tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')))
        print("\n\nAbstract" + str(tree.xpath("//p[@id='sp0005']")) +"\n\n")
        paperTitle = str(tree.xpath("//h1[@class = 'svTitle']/text()"))
        journal = str(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()"))
        authors = tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')
        abstract = str(tree.xpath("//p[@id='sp0005']/text()"))
        try:
                emails = tree.xpath("//li/a[@class='auth_mail']/@href")
                list1.append([url,paperTitle,journal,authors,emails])
        except:
                print("none has a valid email")
##                missedlist.append(url)
##                print("missed may be an index page!")
#continue
print(list1)

#Paper Name 						= tree.xpath("//h1[@class = 'svTitle']/text()")
#list of authors 					= tree.xpath('//ul[@class = "authorGroup noCollab"]/li')
# Journal Name 						= tree.xpath('//div[@class="title"]')
#list of mails AN author 			= tree.xpath('//li[3]/a[@class = "auth_mail"]/@href')
#abstract 							= tree.xpath("//p[@id='sp0005']")

############## IMPORTING DATA ##################
