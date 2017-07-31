from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import sys
import credentials
from datetime import datetime
import numpy as np
import cPickle

arg1 = "0"
if (len(sys.argv) == 2):
    arg1 = sys.argv[1]
else:
    print ("Usage: python extract_features.py [botnum]")
    exit()

url_pre = "https://twitter.com/"
handle_pre = "summerRB"
url_post = "/following"
url = url_pre + handle_pre + arg1 + url_post

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

body = driver.find_element_by_tag_name('body')
for _ in range(50):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

actions = ActionChains(driver)
people = driver.find_elements_by_class_name('ProfileCard-screennameLink')
# people = people[1:] # remove empty first element
people = [person.text for person in people]

logo = driver.find_element_by_class_name("Icon--home")
actions.key_down(Keys.COMMAND).click(logo).key_up(Keys.COMMAND).perform() #  create a new tab

records = []
for x in xrange(len(people)):
    features = np.zeros(25)
    i = 0 # index for features
    print "opening person" + str(x)
    time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[-1]) # now at user page
    driver.get("http://twitter.com/"+str(people[x][1:]))
    bio = driver.find_element_by_class_name("ProfileHeaderCard-bio")
    time.sleep(3)
    stream = driver.find_element_by_class_name("stream-items")
    tweets = stream.find_elements_by_class_name("tweet")
    for kw in credentials.conservative:
        time.sleep(1)
        if kw in bio.text.lower():
            features[i] = 1
        else:
            for y in xrange(5):
                if kw in tweets[y].text.lower():
                    print tweets[y].text
                    time.sleep(3)
                    features[i] = 1
                    break
        i += 1

    for kw in credentials.liberal:
        if kw in bio.text.lower():
            features[i] = 1
        else:
            for y in xrange(5):
                if kw in tweets[y].text.lower():
                    features[i] = 1
                    break
        i += 1
    records.append(features)
    print("closed person %d", x)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

records_arr = np.array(records)
cPickle.dump(records_arr, open("records0.p","wb"))
driver.quit()