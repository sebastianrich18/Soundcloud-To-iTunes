from mp3_tagger import mp3
import requests
import eyed3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def metaDataFromUrl(url):
    arr = url.split('/')[3:]
    obj = {'artist': '', 'title': '', 'album': ''}
    title = arr[1]
    title = title.split('?')[0]
    title = title.split('-')[1].replace('-', ' ')
    obj['artist'] = arr[0].replace('-', ' ').title()
    obj['title'] = title.title()
    try:
        obj['album'] = arr[-1].replace('-', ' ').title()
    except:
        print('Could not find album')

    return obj

def type(path, text): # wait for element to load then type
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
        driver.find_element_by_xpath(path).send_keys(text)
    except TimeoutException:
        print("Failed to load", path)

def click(path): # wait for element to load then click
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
        driver.find_element_by_xpath(path).click()
    except TimeoutException:
        print("Failed to load", path)

link = 'https://soundcloud.com/synnrmusic/10-yellow-tape' #input("Paste link: ")

options = Options()
options.add_argument("--headless") # makes chrome window not show
driver = webdriver.Chrome(options=options)
driver.get('https://www.klickaud.co/')

type('//*[@id="header"]/div/div[1]/div[1]/form/input[1]', link)

driver.find_element_by_xpath('//*[@id="btn"]').click()

print("Found song")
downloadLink = driver.find_element_by_xpath('//*[@id="header"]/div/div/div[1]/div/div[3]/table/tbody/tr/td[2]/a').get_attribute("href")

r = requests.get(downloadLink)

songData = metaDataFromUrl(link)

fileName = '%s.mp3'%(songData['title'])
open('songs/' + fileName, 'wb').write(r.content)
print("Downloaded song")

artLink = driver.find_element_by_xpath('//*[@id="header"]/div/div/div[1]/div/table/tbody/tr/td[1]/img').get_attribute('src')
r = requests.get(artLink)
open('artwork/' + 'art.jpg', 'wb').write(r.content)
print('Downloaded art')

mp3 = eyed3.load('songs/'+fileName)

if (mp3.tag == None):
    mp3.initTag()

mp3.tag.title = songData['title']
mp3.tag.artist = songData['artist']
if songData != '':
    mp3.tag.album = songData['album']
mp3.tag.images.set(3, open('artwork/art.jpg','rb').read(), 'image/jpeg')
mp3.tag.save(version=eyed3.id3.ID3_V2_3)
print('saved tags')

driver.quit()

