from lxml import html
import requests 

reqn = 0
reqn += 1 
print (str(reqn) + " Requests made so far!")
page = requests.get('https://dl.dropboxusercontent.com/u/7333305/test.html')
tree = html.fromstring(page.text)


#class="browseList browseColFirst"


data_journal = []
#[[journal name, path]] 

names = tree.xpath('//th[@class="browseList browseColFirst"]/span/a/text()' )
#price+ \ = tree.xpath('//span[@class="fk-font-17 fk-bold"]/text()')


href = tree.xpath('//th[@class="browseList browseColFirst"]/span/a/@href' )



print (str(len(names)) + ' items crawled!')

f = open('gh.csv','w')
j = 0
for i in range(0,len(names)):
  if 'journal' in href[i]:
    f.write(href[i]+'\n')
    data_journal.append([names[i],href[i]])
    j+=1
print (str(j) +  ' journals found!')

######################### Journal Page ###############################


## pass journal name , url , >> vols
all_issues = []
## journal, journal link,issue issue_details, issue_link
data_journal2 = []
for i in range(0,1):
  data_journal2.append(data_journal[i])
  
for item in data_journal2:  
  print (item)
  reqn += 1 
  print (str(reqn) + " Requests made so far!" )
  page = requests.get('http://www.sciencedirect.com'+item[1])
  tree = html.fromstring(page.text)
  temp = tree.xpath('//a[@aria-expanded = "false"]/@href')
  issue_link= tree.xpath('//div[@class="txt currentVolumes"]/a/@href' )
  issue_detail = tree.xpath('//div[@class="txt currentVolumes"]/text()')
  get_list = []
  for jj in range(0,len(temp)):
    if 'journal' in temp[jj]: 
      get_list.append(temp[jj])
  print ("2:" + str(len(get_list)))
  for link in get_list:
   # print "3:"
    reqn += 1 
    print (str(reqn) + " Requests made so far!")
    
    page2 = requests.get('http://www.sciencedirect.com'+link)
    tree2 = html.fromstring(page2.text)
    issue_links_loop= tree2.xpath('//div[@class="txt currentVolumes"]/a/@href' )
    issue_details_loop = tree2.xpath('//div[@class="txt currentVolumes"]/text()')
    for jj in range(0,len(issue_links_loop)):
      all_issues.append([item[0],item[1],issue_links_loop[jj],issue_details_loop[jj]])
  for jj in range(0,len(issue_link)):
    all_issues.append([item[0],item[1],issue_link[jj],issue_detail[jj]])
  
for i in range(0,len(all_issues)):
  print (all_issues[i])



######################################################################
for item in all_issues:
  if ' 201' in item[3]:
    reqn += 1 
    print (str(reqn) + " Requests made so far!")
    page3 = requests.get('http://www.sciencedirect.com'+item[2])
    tree3 = html.fromstring(page3.text)
    paper_links = tree3.xpath('//a[@class="cLink artTitle S_C_artTitle "]/@href')
    print (paper_links)
    papers = tree3.xpath('//a[@class="cLink artTitle S_C_artTitle "]/text()' )
    print (papers)
    for jj in range(0,min(len(papers),len(paper_links))): 
      all_papers.append([item[0],item[1],item[2],item[3],paper_links[jj],papers[jj]])



for item in all_papers:
  print (item)
for all_paper in all_papers:
  print (all_paper[0],all_paper[3],all_paper[5])
  
  
######################### Crawling for mails #########################
