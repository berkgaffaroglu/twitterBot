from selenium import webdriver
import time
import random

browser = webdriver.Chrome()
browser.get('https://twitter.com/home')
time.sleep(5)
python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
python_button.send_keys('')
python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
python_button.send_keys('')
python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div')
python_button.click()
time.sleep(5)
def randomTweet(tag):
    humanWay = ['içerisi çok pis','mahkum','yasa','eşitlik','insanlık','insaf','merhamet','haftaya','aylardır','günlerdir','saatlerdir','isteyen','mantıklı','el insaf','umut','bırakın','talep görüyor','talebi karşılayın','artık daha ne bekliyorsunuz bilmiyorum']
    tweetList = [f'{tag} hadi arkadaşlar bastıralım',f'Noldu rahat mısınız arkadaşlar mahkumumuz içerde! {random.choice(humanWay)}{tag}',f'Eşit yasa istiyoruz {random.choice(humanWay)} {tag}',f'Olması gereken bu herkes bekliyor {random.choice(humanWay)} {tag}', f'İnsanlar bıktılar  artık verinde herkes rahatlasın {random.choice(humanWay)} {tag}',f'Az kaldı arkadaşlar tweet atmaya devam {random.choice(humanWay)}! {tag}',f'Bizi sonsuza kadar görmezden gelemezler {random.choice(humanWay)} {tag}',f'Size yasa verilmediği sürece tweet atmaya devam! {random.choice(humanWay)} {tag}']

    return random.choice(tweetList)
def tweet():
    browser.get('https://twitter.com/compose/tweet')
    time.sleep(1)
    python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
    python_button.send_keys(randomTweet('MeclistenEşit 5YılCezaindirimi Cezaevleri MezarOlmasın'))
    python_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
    python_button.click()
    time.sleep(3)

while True:
    tweet()
    time.sleep(200)
