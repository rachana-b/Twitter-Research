from selenium import webdriver
import credentials
import time
import numpy as np
import cPickle
import re
from collections import Counter

f1 = open("bios1_test.txt", "r")
f2 = open("bios2_test.txt", "r")
outfile1 = open("bios1_out.txt","wb")
outfile2 = open("bios2_out.txt","wb")

people1 = []
for line in f1:
    toks = line.split()
    if len(toks) > 1:
        people1.append(toks[1])

people2 = []
for line in f2:
    toks = line.split()
    if len(toks) > 1:
        people2.append(toks[1])

# outfile1.write(str(people1))
# outfile2.write(str(people2))


# LOG INTO TWITTER
driver = webdriver.Chrome()

time.sleep(0.3)
driver.get('http://www.twitter.com')


records1 = []
for x in range(1, len(people1)-1):
    features = np.zeros(25)
    i = 0 # index for features
    print "opening person" + people1[x]
    try:
        driver.get("http://twitter.com/"+str(people1[x][1:]))
        time.sleep(0.1)
        bio = driver.find_element_by_class_name("ProfileHeaderCard-bio")
        stream = driver.find_element_by_class_name("stream-items")
        tweets = stream.find_elements_by_class_name("tweet")
        tweets = [tweet.text for tweet in tweets]
        print "trying"
        wanted = credentials.conservative + credentials.liberal

        words = re.findall('\w+', bio.text.lower())
        for tweet in tweets:
            words += re.findall('\w+', tweet.lower())

        cnt = Counter()
        for kw in wanted:
            cnt[kw] = 0
        for word in words:
            if word in wanted:
                cnt[word] += 1

        records1.append(cnt.values())
        print("closed person %d", x)

    except Exception as e:
        del people1[x]

records2 = []
for x in range(1, len(people2)-1):
    features = np.zeros(25)
    i = 0 # index for features
    print "opening person" + people2[x]
    try:
        driver.get("http://twitter.com/"+str(people1[x][1:]))
        time.sleep(0.1)
        bio = driver.find_element_by_class_name("ProfileHeaderCard-bio")
        stream = driver.find_element_by_class_name("stream-items")
        tweets = stream.find_elements_by_class_name("tweet")
        tweets = [tweet.text for tweet in tweets]
        wanted = credentials.conservative + credentials.liberal

        words = re.findall('\w+', bio.text.lower())
        for tweet in tweets:
            words += re.findall('\w+', tweet.lower())

        cnt = Counter()
        for kw in wanted:
            cnt[kw] = 0
        for word in words:
            if word in wanted:
                cnt[word] += 1

        records2.append(cnt.values())
        print("closed person %d", x)

    except Exception as e:
        del people2[x]

records_arr1 = np.array(records1)
records_arr2 = np.array(records2)
cPickle.dump(records_arr1, open("records1_half.p","wb"))
cPickle.dump(records_arr2, open("records2_half.p","wb"))
driver.quit()