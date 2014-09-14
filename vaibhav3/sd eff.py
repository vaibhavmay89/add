from lxml import html
import requests 

reqn = 0 
########### FILE WRITER ###################
start = 121
end = 150

# [44,54,73,77,151,158,324,347,363,720,1557]

file = open("papers.txt","a")
file.write("\n")
file.close()

file = open("logs.txt","a")
file.write("\nstart: "+str(start)+"\n end: "+str(end)+"\n\n\n\n\n")
file.close()



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




######################### PRINTER #########################


def printer(string):
	print(string)
	writefile("logs.txt",string)


#################### URL OPENER ########################

def openurl(url): 
	global reqn
	reqn +=1
	printer (str(reqn) + " Requests made so far!")
	page = requests.get(str("http://www.sciencedirect.com"+url)	)
	#page = requests.get('https://dl.dropboxusercontent.com/u/7333305/test.html')
	tree = html.fromstring(page.text)
	return tree
def checkyr(string):
	if (("2015" in string) or ("2014" in string) or ("2013" in string) or ("2012" in string)):
		return 1
	return 0  
papers = []
def crawlpapers(tree,string = ""):
	global papers
	##printer(papers)
	open_papers = tree.xpath("//li[@class='title ']/h4/a/@href")
	for i in range(0,len(open_papers)): 
		##printer(len(open_papers[i]))
		papers.append(open_papers[i])
		writefile("papers.txt",str(open_papers[i])+","+string)

	
	## append in a file 
def crawlIssues(tree):
		crawlpapers(tree)
		open_issues_text = tree.xpath("//div[@id='volumeIssueData']/ol/li/ol/li/div[@class='txt currentVolumes']/text()")
		open_issues = tree.xpath("//div[@class='txt currentVolumes']/a/@href")

		for i in range(0,len(open_issues)):
			print ("<"+str(i)+">")
			if checkyr(open_issues_text[i]) == 1:
				crawlpapers(openurl(open_issues[i]),open_issues_text[i])
			else:
				continue


page = requests.get("https://dl.dropboxusercontent.com/u/7333305/test.html")	
#page = requests.get('https://dl.dropboxusercontent.com/u/7333305/test.html')
tree = html.fromstring(page.text)
href = tree.xpath('//th[@class="browseList browseColFirst"]/span/a/@href' )
name = tree.xpath('//th[@class="browseList browseColFirst"]/span/a/text()' )
journals = []
names= []

for i in range(0,len(href)):
	if "journal" in href[i]:
		journals.append(href[i])
		names.append(name[i])
		

printer (str(len(journals))+ " Journals found!") 


for i in range(0,len(journals)):
        print(journals[i]+","+names[i])
for i in [54,223]:#(start,end):
	print ("<<"+str(i)+">>")
	tree = openurl(journals[i])
	open_vol = tree.xpath('//a[@aria-expanded = "true"]/@title')
	if checkyr(str(open_vol)) ==0 :
		printer ("SJ: The Journal with url:"+journals[i] +" and title: "+ str(open_vol) +" is outdated !!")   
		continue
	else: 
		crawlpapers(tree)
		closed_vols = tree.xpath('//a[@aria-expanded = "false" and @class ="volLink"]/text()')
		##printer(closed_vols)
		closed_vols_url = tree.xpath('//a[@aria-expanded = "false" and @class ="volLink"]/@href')
		for j in range(0,len(closed_vols)):
			if checkyr(closed_vols[j]) ==1:
				crawlIssues(openurl(closed_vols_url[j]))
			else:
				printer ("SV: The Volume with url: "+closed_vols_url[j] +" and title: "+ str(closed_vols[j]) +"  is outdated !!")



		

