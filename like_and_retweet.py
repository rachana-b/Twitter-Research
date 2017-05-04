import time
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random

sample_num = 25

num = "0"
if (len(sys.argv) == 2):
	num = sys.argv[1]
else:
	print ("Usage: python follow_recommended.py [botnum]")
	exit()

url = "https://twitter.com/home"
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
for _ in range(30):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.5)

# for _ in range(20):
# 	body.send_keys(Keys.PAGE_UP)
# 	time.sleep(0.3)


fav_class_name = 'ProfileTweet-actionButton.js-actionButton.js-actionFavorite'
# get the favorite buttons and click a random sample of them
favorites = browser.find_elements_by_class_name(fav_class_name)
print(len(favorites))
for c in range(0, min(len(favorites), sample_num)):
	#browser.execute_script("arguments[0].scrollIntoView();", favorites[c])
	if favorites[c].is_displayed():
		favorites[c].click()
		print("%s: Like Button Clicked" % (usr+num,))
	else:
		print("%s: Element Not Visible" % (usr+num,))
	time.sleep(1.0)

# get the retweet buttons and click a random sample of them
# retweets = browser.find_elements_by_class_name('ProfileTweet-actionButton.js-actionButton.js-actionRetweet')
# i = 0
# while (i < sample_num):
# 	if (random.random() < 0.5):
# 		retweets[i].click()
# 		time.sleep(1.0)
# 		button = browser.find_element_by_class_name('btn.primary-btn.retweet-action')
# 		button.click()
# 		i += 1
# 	time.sleep(1.0)
