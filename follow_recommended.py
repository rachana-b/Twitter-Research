import time
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

num = "0"
if (len(sys.argv) == 2):
	num = sys.argv[1]
else:
	print ("Usage: python follow_recommended.py [start botnum] [end botnum]")
	return

url = "https://twitter.com/who_to_follow/suggestions"
usr = "springIWthc"
pwd = "louisasimpson"

# LOG INTO TWITTER
browser = webdriver.Firefox()
time.sleep(1)

browser.get(url)
time.sleep(4)
login1 = browser.find_element_by_class_name("js-username-field")
time.sleep(1)
login2 = browser.find_element_by_class_name("js-password-field")
time.sleep(1)
login1.send_keys(usr + num)
time.sleep(1)
login2.send_keys(pwd)
time.sleep(1)
browser.find_element_by_css_selector("button.submit.btn.primary-btn").click()
time.sleep(3)

# SCROLL DOWN TO LOAD ENTIRE FEED
body = browser.find_element_by_tag_name('body')
for _ in range(100):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.3)

# FIND THE USER HANDLES AND BRIEF BIOS
handles = browser.find_elements_by_class_name('ProfileCard-screenname')
tweets = browser.find_elements_by_css_selector('p.ProfileCard-bio.u-dir')
buttons = browser.find_elements_by_class_name('user-actions-follow-button.js-follow-button.follow-button.btn')

print ("BOT %d RECOMMENDATION LIST AND BIOS" % (num,))
print ("=======================================================================")
for i in range(len(tweets)):
	res = "%-20s %s" % (handles[i].text, tweets[i].text)
	print (res.encode('utf-8', 'ignore'))

# follow all the recommendations
for i in buttons:
	button.click()
	time.sleep(0.5)
print ("Followed %d new accounts" % (len(buttons),))
