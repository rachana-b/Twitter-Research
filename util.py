#import requests
import time
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=/prof")
# browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=options)

browser = webdriver.Firefox()
url = "https://twitter.com/springIWthc3/following"
time.sleep(1)

# r = request.get(url)
# soup = BeautifulSoup(r.tet, 'html.parser')

# tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]

# print(tweets)


browser.get(url)
time.sleep(4)

usr = "thomashikaru"
pwd = "Clovek79!"

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

body = browser.find_element_by_tag_name('body')
for _ in range(40):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.3)

handles = browser.find_elements_by_class_name('ProfileCard-screenname')
tweets = browser.find_elements_by_css_selector('p.ProfileCard-bio.u-dir')

for i in range(len(tweets)):
	res = "%-20s %s" % (handles[i].text, tweets[i].text)
	print (res.encode('utf-8', 'ignore'))


