'''
Author: Rachana Balasubramanian
Description: For following recommended Twitter users. Run on your host machine.
'''

import time
import sys
import selenium
from selenium import webdriver
import credentials
from selenium.webdriver.common.keys import Keys


sample_num = 4

num = "0"
if (len(sys.argv) == 2):
	num = sys.argv[1]
else:
	print ("Usage: python follow_recommended.py [botnum]")
	exit()

url = "https://twitter.com/who_to_follow/suggestions"
usr = "summerRB"
pwd = credentials.PASSWORD

# LOG INTO TWITTER
# driver = webdriver.PhantomJS(executable_path = "/vagrant/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
driver = webdriver.Chrome()

time.sleep(1)

driver.get('http://www.twitter.com')
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
print("Login Sucessfull")

driver.get(url)

# SCROLL DOWN TO LOAD ENTIRE FEED
body = driver.find_element_by_tag_name('body')
for _ in range(4):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.3)

print("scrolled")
a= driver.find_element_by_id("stream-items-id")
lis = a.find_elements_by_css_selector("li") #not all of these are buttons

i = 0
cnt = 0
while (cnt < sample_num):
    print("i = " + str(i) + ", cnt = " + str(cnt))
    time.sleep(1)
    try:
        button = lis[i].find_element_by_css_selector("button")
        button.click()
        cnt += 1
    except Exception as e:
        print("skip")
    i += 1
driver.quit()
