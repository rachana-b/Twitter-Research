# Scrapes a twitter page containing the list of followees of an account
# Modify the usr and pwd fields below with your credentials

import time
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import credentials
from datetime import datetime

arg1 = "0"
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
driver.get('http://www.twitter.com')
time.sleep(2)
login = driver.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')
login[0].click()
user = driver.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')
user[0].send_keys(usr + str(arg1).zfill(2))
user = driver.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')
user.send_keys(pwd)
time.sleep(1)
LOG = driver.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
LOG[0].click()


# LOAD THE FOLLOWERS PAGE
url = url_pre + handle_pre + str(arg1).zfill(2) + url_post
driver.get(url)

# SCROLL DOWN TO LOAD ENTIRE FEED
body = driver.find_element_by_tag_name('body')
for _ in range(100):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.3)

# FIND THE USER HANDLES AND BRIEF BIOS
handles = driver.find_elements_by_class_name('ProfileCard-screenname')
tweets = driver.find_elements_by_css_selector('p.ProfileCard-bio.u-dir')

logpath = "/Users/Rachana_B/workspace/Twitter-Research/classifications/bios" + arg1 + "_"+str(datetime.now())+".txt" 
f = open(logpath, "a")

# print ("BOT %s FOLLOWER LIST AND BIOS" % (arg1,))
# print ("=======================================================================")
# for i in range(len(tweets)):
# 	res = "%-20s %s" % (handles[i].text, tweets[i].text)
# 	print (res.encode('utf-8', 'ignore'))

f.write("BOT %s FOLLOWER LIST AND BIOS" % (arg1,) + "\n")
f.write("=======================================================================\n")
for i in range(len(tweets)):
    res = None
    #TODO: REPLACE WITH ML CLASSIFIER
    if any(word in tweets[i].text.lower() for word in credentials.conservative):
        res = "c %-20s %s" % (handles[i].text, tweets[i].text)
    elif any(word in tweets[i].text for word in credentials.liberal):
        res = "l %-20s %s" % (handles[i].text, tweets[i].text)
    else:
        res = "n %-20s %s" % (handles[i].text, tweets[i].text)
        # driver.find_element_by_tag_name('body').send_keys(Keys.COMAMND + 'w')
    f.write(res.encode('utf-8', 'ignore'))
    f.write("\n")

driver.quit()