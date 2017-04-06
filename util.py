# Scrapes a twitter page containing the list of followees of an account
# Modify the usr and pwd fields below with your credentials
# Takes two command line arguments first and last: the number of the first bot and number of last bot
# assumes that the bots have handles starting with handle_pre (see below) followed by a number
# between first and last
# python util.py 0 5 will scrape information for bots springIWthclark0, ..., springIWthclark5

import time
import sys
#from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

arg1 = "0"
if (len(sys.argv) == 2):
	arg1 = sys.argv[1]
else:
	print ("Usage: python util.py [botnum]")
	exit()

url_pre = "https://twitter.com/"
handle_pre = "springIWthc"
url_post = "/following"
url = url_pre + handle_pre + arg1 + url_post

usr = "thomashikaru"
pwd = "Clovek79!"

# LOG INTO TWITTER
browser = webdriver.Firefox()
time.sleep(1)
browser.get(url)
time.sleep(2)
login1 = browser.find_element_by_class_name("js-username-field")
time.sleep(1)
login2 = browser.find_element_by_class_name("js-password-field")
time.sleep(1)
login1.send_keys(usr)
time.sleep(1)
login2.send_keys(pwd)
time.sleep(1)
browser.find_element_by_css_selector("button.submit.btn.primary-btn").click()
time.sleep(3)


# LOAD THE FOLLOWERS PAGE
# url = url_pre + handle_pre + arg1 + url_post
# browser.get(url)

# SCROLL DOWN TO LOAD ENTIRE FEED
body = browser.find_element_by_tag_name('body')
for _ in range(100):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.3)

# FIND THE USER HANDLES AND BRIEF BIOS
handles = browser.find_elements_by_class_name('ProfileCard-screenname')
tweets = browser.find_elements_by_css_selector('p.ProfileCard-bio.u-dir')

print ("BOT %s FOLLOWER LIST AND BIOS" % (arg1,))
print ("=======================================================================")
for i in range(len(tweets)):
	res = "%-20s %s" % (handles[i].text, tweets[i].text)
	print (res.encode('utf-8', 'ignore'))


