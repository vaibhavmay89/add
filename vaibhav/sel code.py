from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.sciencedirect.com/science/article/pii/S1742706114002360")

#//th[@class='browseList browseColFirst']span/a
t= driver.find_elements_by_xpath("//*[@class='auth_mail']")
for i in range(0,len(t)):
        print (str(t[i].get_attribute("href")))
##       _#_#_#_#_#_#")
##    print (i.get_attribute("value"))
print ("______")

driver.close()

