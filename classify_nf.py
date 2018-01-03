# Scrapes a twitter page containing the list of followees of an account
# Modify the usr and pwd fields below with your credentials

import time
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import credentials
from datetime import datetime

if (len(sys.argv) == 2):
	arg1 = sys.argv[1]
else:
	print ("Usage: python util.py [botnum]")
	exit()

url_pre = "https://twitter.com/"
handle_pre = "summerRB"
url_post = "/following"
url = url_pre + arg1 + url_post

usr = "summerRB"
pwd = credentials.PASSWORD

# LOG INTO TWITTER
driver = webdriver.Chrome()

time.sleep(1)
driver.get('http://www.twitter.com/settings/account')
time.sleep(20)
# login = driver.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')
# login[0].click()
# user = driver.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')
# print(usr + str(arg1).zfill(2))
# # user[0].send_keys(usr + str(arg1).zfill(2))
# user[0].send_keys("summerRB04")
# time.sleep(0.3)
# user = driver.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')
# user.send_keys(pwd)
# time.sleep(1)
# LOG = driver.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
# LOG[0].click()



# LOAD THE FOLLOWERS PAGE
# url = url_pre + handle_pre + str(arg1).zfill(2) + url_post
driver.get(url_pre)

# SCROLL DOWN TO LOAD ENTIRE FEED
body = driver.find_element_by_tag_name('body')
for _ in range(30):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.3)

# FIND THE USER HANDLES AND BRIEF BIOS
container = driver.find_element_by_id("stream-items-id")
tweets =  container.find_elements_by_css_selector(".tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable")

logpath = "/Users/Rachana_B/workspace/Twitter-Research/classifications/bios" + arg1 + "_"+str(datetime.now())+".txt" 
f = open(logpath, "a")


f.write("BOT %s NEWSFEED" % (arg1,) + "\n")
f.write("=======================================================================\n")
# for i in range(len(tweets)):
for i in range(30):
    print(i)
    res = None

    if any(word in tweets[i].text.lower() for word in credentials.conservative):
        res = "\n RACHANA_TAGc %s \n" %(tweets[i].text)
    elif any(word in tweets[i].text.lower() for word in credentials.liberal):
        res = "\n RACHANA_TAGl %s \n" %(tweets[i].text)
    else:
        res = "\n RACHANA_TAGn %s \n" %(tweets[i].text)
        # driver.find_element_by_tag_name('body').send_keys(Keys.COMAMND + 'w')
    print(res)
    f.write(res)
    f.write("\n")

driver.quit()