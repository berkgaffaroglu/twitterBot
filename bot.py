from selenium import webdriver
import time
import random

username = 'test' #username
password = 'password' #password
browser = webdriver.Chrome() 
browser.get('https://twitter.com/home') # Browsing to the twitter.com
time.sleep(5) # This is necessary because selenium can be really slow to detect elements so we are waiting 5 seconds.
python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
python_button.send_keys(username)
python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
python_button.send_keys(password)
python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div')
python_button.click()
time.sleep(5) # Again, we are waiting for the page.

def randomTweet(tag): # This function allows us to generate random tweets.
    moreHuman = ['life','we','probably'] # This is also neccesary because twitter doesn't allow us to post the same tweet that we tweeted already.
    tweetList = [f'Life is good {random.choice(moreHuman)}{tag}', f'I am happy{random.choice(moreHuman)} {tag}'}
    return random.choice(tweetList)
                 
def tweet(): # This is the actual part that we tweet.
    browser.get('https://twitter.com/compose/tweet') # Twitter's current tweeting page.
    time.sleep(1) # Browsing might take 1 second or less so we are waiting 1 second.
    python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
    python_button.send_keys(randomTweet('')) # This could be any tag.
    python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
    python_button.click()

while True: # This is an infinite loop, so it will not stop tweeting.
    tweet() # We are calling the function tweet()
    time.sleep(200) # How long should program wait until the next tweet. This on you.
