from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference('permissions.default.stylesheet', 2)
#firefox_profile.set_preference('permissions.default.image', 2)
#firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver = webdriver.Firefox(firefox_profile=firefox_profile)
journal = []
data = []
url = "http://www.sciencedirect.com/science/article/pii/S1359645414005989"
file = open('data.txt','r')
lines = file.readlines()
print(type(lines))
for line in lines:
    line.replace('\n','')
    data.append(line)
print (data[0],len(data))


i=0
ii = 0
package = []
for url in data:
    print (str(ii) +url+"\nLen: "+str(len(package)))
    ii+=1
    driver.get(url)
    journal = driver.find_elements_by_xpath('//div[@class="title"]')
    issue = driver.find_elements_by_xpath("//p[@class='volIssue']")
    title = driver.find_elements_by_xpath("//h1[@id='tm005']")
    numberOfAuthors = len(driver.find_elements_by_xpath("//li[@class='smh5']"))

    i = 0
    while(i<=2 and numberOfAuthors ==0):
        time.sleep(2*i)
        print(i)
        driver.get(url)
        numberOfAuthors = len(driver.find_elements_by_xpath("//li[@class='smh5']"))
        print (numberOfAuthors)
        
        i+=1
    package = []
    for i in range(0,numberOfAuthors):

        aut_email = driver.find_elements_by_xpath("//li[@class='smh5'][" +str(i+1)+"]/a[@class='auth_mail']")
        aut_name = driver.find_elements_by_xpath("//li[@class='smh5'][" +str(i+1)+"]/a[@class='authorName']")
        mailing = []
        if len(aut_email)>0:
            for mail in aut_email:
                print(i,mail.get_attribute("href"),aut_name[0].text)
                mailing.append(mail.get_attribute("href"))
            package.append([[journal[0].text,issue[0].text,title[0].text,aut_name[0].text,int(aut_name[0].get_attribute("data-pos"))],[mailing]])
            file = open("packets.txt","a")
            try:
                file.write(str(i))
            except:
                continue
##        print(str(i) +": "+"//li[@class='smh5'][" +str(i+1)+"]/a[@class='auth_mail']/@href")
##    print(issue[0].text)
##    print(title)
##    print(journal[0].text)
##    print(numberOfAuthors)
    
for i in package:
    file = open("packets.txt","a")
    try:
        file.write(str(i))
    except:
        continue


## file for articles: ID, Journal Name, Issue, Title, URL,Tut_ID
## file for authors:  ID, Name, email list,len(email_list)
