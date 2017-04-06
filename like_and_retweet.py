import time
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random

sample_num = 10

num = "0"
if (len(sys.argv) == 2):
	num = sys.argv[1]
else:
	print ("Usage: python follow_recommended.py [botnum]")
	exit()

url = "https://twitter.com"
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
for _ in range(10):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(1)

# get the favorite buttons and click a random sample of them
favorites = browser.find_elements_by_class_name('ProfileTweet-actionButton.js-actionButton.js-actionFavorite')
i = 0
while (i < sample_num):
	if (random.random() < 0.5):
		favorites[i].click()
		i += 1
	time.sleep(1.0)

# get the retweet buttons and click a random sample of them
retweets = browser.find_elements_by_class_name('ProfileTweet-actionButton.js-actionButton.js-actionRetweet')
i = 0
while (i < sample_num):
	if (random.random() < 0.5):
		retweets[i].click()
		i += 1
	time.sleep(1.0)