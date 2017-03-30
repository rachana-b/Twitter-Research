import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# url = u'https://twitter.com/'

# r = request.get(url)
# soup = BeautifulSoup(r.tet, 'html.parser')

# tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]

# print(tweets)


browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(5):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.2)

tweets = broswer.find_element_by_class_name('tweet-text')

for tweet in tweets:
	print(tweet.text)