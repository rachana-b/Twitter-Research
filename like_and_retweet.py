import time
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import credentials

sample_num = 2

num = "0"
if (len(sys.argv) == 3):
	num = sys.argv[1]
	flag = sys.argv[2]
elif (len(sys.argv) == 2):
	num = sys.argv[1]
	flag = "None"
else:
	print ("Usage: python like_and_retweet.py [botnum] [flag]")
	exit()

url = "https://www.twitter.com"
usr = "summerRB"
pwd = credentials.PASSWORD

# LOG INTO TWITTER
driver = webdriver.Chrome()
time.sleep(1)

driver.get(url)
time.sleep(2)
login = driver.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')
login[0].click()
user = driver.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')
user[0].send_keys(usr + str(num).zfill(2))
user = driver.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')
user.send_keys(pwd)
time.sleep(1)
LOG = driver.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
LOG[0].click()

# SCROLL TO LOAD ENTIRE FEED
body = driver.find_element_by_tag_name('body')
for _ in range(12):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.5)

for _ in range(20):
    body.send_keys(Keys.PAGE_UP)
    time.sleep(0.3)

# get the favorite buttons and click a random sample of them
container = driver.find_element_by_id("stream-items-id")
tweets =  container.find_elements_by_css_selector(".tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable")
favorites = container.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")
retweets = container.find_elements_by_css_selector('.ProfileTweet-actionButton.js-actionButton.js-actionRetweet')
print("favorites " + str(len(favorites)) + " tweets " + str(len(tweets)) + " retweets " + str(len(retweets)))
if len(favorites) != len(tweets):
	print("tweets != favorites")
	driver.quit()
	exit()

if flag == "None":
	cnt = 0 # only need like counter, since "index" is randomly generated
	while cnt < min(len(favorites), sample_num):
	# for x in range(0, min(len(favorites), sample_num)):
		c = random.randrange(len(favorites))
		try:
			if "Promoted" not in tweets[i].text:
				print(favorites[c].text)
				favorites[c].click()
				print("%s: Like Button Clicked" % (usr+num,))
				cnt += 1 # counter only updates if you actually liked something
		except Exception as e:
			print(favorites[c].text + " EXCEPTION")
		time.sleep(1)

	# get the retweet buttons and click a random sample of them
	i = 0
	cnt = 0
	while (cnt < sample_num):
		x = random.random()
		print(x)
		time.sleep(2)
		if ((x < 0.5) and ("Promoted" not in tweets[i].text)):
			try:
				retweets[i].click()
				time.sleep(1.0)
				button = retweets[i].find_element_by_xpath('//*[@id="retweet-tweet-dialog-dialog"]/div[2]/form/div[2]/div[3]/button')
				button.click()
				cnt += 1
				print("clicked retweet dialogue")
			except Exception as e:
				print(Exception)
				print(str(i) + " button was " + retweets[i].text)
		else:
			print("don't click")
		time.sleep(1.0)
		i += 1

else:
	if flag == 'c':
		keywords = credentials.conservative
	elif flag == 'l':
		keywords = credentials.liberal
	else:
		print("invalid flag")
		exit()

	i = 0
	cnt = 0 # only need like counter, since "index" is randomly generated
	while cnt < min(len(favorites), sample_num):
		try:
			print(tweets[i].text)
			time.sleep(5)
			if any(word in tweets[i].text for word in keywords) and ("Promoted" not in tweets[i].text):
				favorites[i].click()
				print("%s: Like Button Clicked" % (usr+num,))
			cnt += 1 # counter only updates if you actually liked something
		except Exception as e:
			print(favorites[c].text + " EXCEPTION")
		time.sleep(1)
		i += 1
	# get the retweet buttons and click a random sample of them
	i = i - sample_num/2
	cnt = 0
	while cnt < min(len(retweets), sample_num):
		try:
			if any(word in tweets[i].text for word in keywords) and "Promoted" not in tweets[i].text:
				time.sleep(1)
				retweets[i].click()
				print(tweets[i].text)
				time.sleep(5.0)
				button = retweets[i].find_element_by_xpath('//*[@id="retweet-tweet-dialog-dialog"]/div[2]/form/div[2]/div[3]/button')
				button.click()
				cnt += 1
				print("clicked retweet dialogue")
		except Exception as e:
			print(Exception)
			# print(str(i) + " button was " + retweets[i].text)
		i += 1

driver.quit()
