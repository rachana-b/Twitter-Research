#!/n/fs/ugrad/ug18/rachanab/sum2017research/bin/python

#########
from __future__ import absolute_import
#########

from selenium import webdriver
from xvfbwrapper import Xvfb
import os
import time

import credentials

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


import random


def ensure_firefox_in_path():
    """
    If ../../firefox-bin/ exists, add it to the PATH.
    If firefox-bin does not exist, we throw a RuntimeError.
    """

    ffbin = os.path.abspath("/u/bl6/thesis/firefox-bin")
    if os.path.isdir(ffbin):
        curpath = os.environ["PATH"]
        if ffbin not in curpath:
            os.environ["PATH"] = ffbin + os.pathsep + curpath
    else:
        raise RuntimeError(
            "The `firefox-bin` directory is not found.")
    '''
    mongobin = os.path.abspath("/u/bl6/thesis/firefox-bin/mongodb/bin")
    if os.path.isdir(mongobin):
        curpath = os.environ["PATH"]
        if mongobin not in curpath:
            os.environ["PATH"] = mongobin + os.pathsep + curpath
    else:
        raise RuntimeError(
            "The `mongodb-linux-x86_64-3.4.10` directory is not found.")
    '''


class SeleniumBot():

    def __init__(self, username, password, num):
        ensure_firefox_in_path()
        self.num = num
        self.xvfb = Xvfb(width=1280, height=720)
    
        self.xvfb.start()

        binary = FirefoxBinary('/u/rachanab/sum2017_research/firefox-bin/firefox')
        self.browser = webdriver.Firefox(firefox_binary=binary)

        # self.browser = webdriver.Firefox()

        #log into certain bot
        url = 'https://twitter.com/settings/account'
        time.sleep(1)
        self.browser.get(url)
        time.sleep(4)
        login1 = self.browser.find_element_by_class_name("js-username-field")
        time.sleep(1)
        login2 = self.browser.find_element_by_class_name("js-password-field")
        time.sleep(1)
        login1.send_keys(username)
        time.sleep(1)
        login2.send_keys(password)
        time.sleep(1)
        # submit button
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button").click()
        time.sleep(3)
      
    
    def leave(self): 
        self.browser.quit()
        self.xvfb.stop()

    #https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python/43299513
    def _scroll_completely_down(self):
        driver = self.browser
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        i = 0 
        while i < 2:
            i = i + 1
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def get_tweets(self):
        self.browser.get('https://twitter.com')
        #get all the tweets
        tweets = self.browser.find_elements_by_class_name('tweet')
        print(tweets)
        print(len(tweets))
        text = []

        for i in range(min(len(tweets), 15)):
            text.append(tweets[i].text)
        print(text)


    def retweet(self):
        self.browser.get('https://twitter.com')
        #get all the tweets
       # tweets = self.browser.find_element_by_css_selector('#stream-item-tweet-935947628092841984 > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)')
        tweet = self.browser.find_element_by_css_selector(".js-stream-item .ProfileTweet-action--retweet div")
        time.sleep(3)
        tweet.click()
        time.sleep(3)

        self.browser.save_screenshot("screenshotretweet_3.png")

        confirm_button = self.browser.find_element_by_class_name('EdgeButton.EdgeButton--primary.retweet-action')
        time.sleep(3)
        confirm_button.click()
        self.browser.save_screenshot("screenshot2retweet_3.png")

    def tag_retweet(self, flag, sample_num):
            if flag == 'c':
                keywords = credentials.conservative
            elif flag == 'l':
                keywords = credentials.liberal
            else:
                print("invalid flag")
                exit()

            container = self.browser.find_element_by_id("stream-items-id")
            tweets =  container.find_elements_by_css_selector(".tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable")
            retweets = container.find_elements_by_css_selector('.ProfileTweet-actionButton.js-actionButton.js-actionRetweet')

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

    #interior part of button
    def follow_user(self, username):
        self.browser.get('https://twitter.com/' + username)
        time.sleep(4)
        #a = self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[7]/div/div/span[2]/button[1]")
        a = self.browser.find_element_by_class_name("EdgeButton.EdgeButton--secondary.EdgeButton--medium.button-text.follow-text")
        
        time.sleep(3)
        while True:
            print(a.text)
            a.click()
            time.sleep(3)
            return

    def click_on_link(self):
        '''
        self.browser.get('https://twitter.com/')
        time.sleep(3)

        self.browser.save_screenshot("screenshotscrolldown.png")
        
        a = self.browser.find_elements_by_class_name("js-stream-item.stream-item.stream-item")
        print(len(a))
        a[0].click()
        time.sleep(3)
        '''
    
        self.browser.get("https://twitter.com/senorrinhatch/status/939672194271072256")
        time.sleep(20)
        self._scroll_completely_down()
        time.sleep(20)
        self.browser.save_screenshot("screenshotlink.png")
        #a = self.browser.find_element_by_class_name("TwitterCardsGrid.TwitterCard.TwitterCard--animation")
        #c = self.browser.find_element_by_class_name("TwitterCardsGrid-col--12.TwitterCardsGrid-col--spacerBottom.CardContent")
        #d = c.find_element_by_css_selector("js-openLink.u-block.TwitterCardsGrid-col--12.TwitterCard-container.TwitterCard-container--clickable.SummaryCard--large")
        #d = self.browser.find_element_by_xpath("/html/body/div/div/a")
       # d = self.browser.find_element_by_class_name("u-block")
        d = self.browser.find_elements_by_tag_name("iframe")
        print(len(d))
        time.sleep(3)
        for iframe in d:
            print(iframe.get_attribute("id"))
            print(iframe.get_attribute("src"))
        time.sleep(3)
        self.browser.get("https://twitter.com/i/cards/tfw/v1/939672194271072256?cardname=summary_large_image&autoplay_disabled=true&earned=true&edge=true&lang=en&card_height=344&scribe_context=%7B%22client%22%3A%22web%22%2C%22page%22%3A%22permalink%22%2C%22section%22%3A%22permalink%22%2C%22component%22%3A%22tweet%22%7D&bearer_token=AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%252F40K4moUkGsoc%253DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw#xdm_e=https%3A%2F%2Ftwitter.com&xdm_c=default910&xdm_p=1")
        time.sleep(3)
        self.browser.save_screenshot("clicked_link.png")

    #this works but its every other; also cant trust last one
    def find_name(self):
        self.browser.get('https://twitter.com')
        #get all the tweets 
        tweets = self.browser.find_elements_by_class_name('tweet')
        for i in range(min(len(tweets), 15)):
            print(tweets[i].text)
            username = tweets[i].get_attribute('data-retweeter')
            if not username:
                username = tweets[i].get_attribute('data-screen-name')
            print("####")
            print(username)
            print("####")

    #this works for retweets only 
    def find_name_2(self):
        self.browser.get('https://twitter.com/')
        a = self.browser.find_elements_by_class_name("pretty-link.js-user-profile-link")
        for b in a:
            print(b.get_attribute("href"))

    #TwitterCard-title.js-cardClick.tcu-textEllipse--multiline
           # js-openLink u-block TwitterCardsGrid-col--12 TwitterCard-container TwitterCard-container--clickable SummaryCard--large
    def follow_users(self):
        print("Follow Users")
        client = MongoClient()
        db = client.poldatabase
        collection = db.followees
        a = collection.find()
        i = 0
        for b in a:
            i = i + 1
            if self.num not in b['bots']:
                print(i)
                #print(b['name'])
                self.follow_user(b['name'])
                b['bots'] = b['bots'] + [self.num]
                collection.update({'_id': b['_id']}, b)
                time.sleep(random.randrange(5, 10))


def click_to_element(element, sleep_after=0.5):
    """Click to element and handle WebDriverException."""
    try:
        element.click()
        time.sleep(sleep_after)
    except WebDriverException:
        pass


def move_to_element(driver, element):
    try:
        ActionChains(driver).move_to_element(element).perform()
    except WebDriverException:
        pass


def scroll_to_element(driver, element):
    try:
        driver.execute_script("window.scrollTo(%s, %s);" % (
            element.location['x'], element.location['y']))
    except WebDriverException:
        pass


def move_to_and_click(driver, element, sleep_after=0.5):
    """Scroll to the element, hover over it, and click it"""
    scroll_to_element(driver, element)
    move_to_element(driver, element)
    click_to_element(element, sleep_after)
    return
def wait_and_find(driver, locator_type, locator,
                  timeout=3, check_iframes=True):
    """Search for element with `locator` and block if not found
    Parameters
    ----------
    driver : selenium.webdriver.firefox.webdriver.WebDriver
        An instance of the Firefox webdriver
    locator_type : string
        A text representation of the attribute to search by, e.g. searching
        by `id`, `class name`, and so on. For a list of supported types,
        `import selenium.webdriver.common.by.By` and use `By.LINK_TEXT`,
        `By.ID`, and so on.
    locator : string
        The search string used to identify the candidate element.
    timeout : int, optional
        Time in seconds to block before throwing `NoSuchElementException`. The
        default is 3 seconds.
    check_iframes : bool, optional
        Set to `True` to also check all iframes contained directly in the
        current frame.
    Returns
    -------
    selenium.webdriver.firefox.webelement.FirefoxWebElement
        Matching element (if any is found before `timeout`).
    Raises
    ------
    NoSuchElementException
        Raised if no element is located with `locator` before `timeout`.
    """
    if is_found(driver, locator_type, locator, timeout):
        return driver.find_element(locator_type, locator)
    else:
        if check_iframes:  # this may return the browser with an iframe active
            driver.switch_to_default_content()
            iframes = driver.find_elements_by_tag_name('iframe')

            for iframe in iframes:
                driver.switch_to_default_content()
                driver.switch_to_frame(iframe)
                if is_found(driver, locator_type, locator, timeout=0):
                    return driver.find_element(locator_type, locator)

            # If we get here, search also fails in iframes
            driver.switch_to_default_content()
        raise NoSuchElementException("Element not found during wait_and_find")


def is_found(driver, locator_type, locator, timeout=3):
    try:
        w = WebDriverWait(driver, timeout)
        w.until(lambda d: d.find_element(locator_type, locator))
        return True
    except TimeoutException:
        return False

b = SeleniumBot('summerRB00', 'RBbot2017', 10)
#b.click_on_link()
#b.find_name()
#b.follow_users()
#b.click_on_link()
b.tag_retweet('c', 3)
b.leave()



