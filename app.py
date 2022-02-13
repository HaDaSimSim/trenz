from lib2to3.pgen2 import driver
from time import time
from TikTokApi import TikTokApi
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import urllib.request
import subprocess
import shutil
import time
import pyautogui
import os
import sys
import getpass
import random

GMAIL = '...@gmail.com'
PASSWORD = '...'
NTH = 2

defaultTitle = [
    'it\'s trending on tiktok xD',
    'wow how do this??',
    'it\'s so amazing!',
    'cool :O',
    'trending on tiktok now!',
    'tiktok trend!',
    'on trend'
]

try:
    shutil.rmtree(r"C:\chrometemp")
except FileNotFoundError:
    pass

try:
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')
except FileNotFoundError:
    subprocess.Popen(r'C:\Users\{0}\AppData\Local\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"'.format(getpass.getuser()))

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

driver.implicitly_wait(15)
driver.get('https://studio.youtube.com/')
pyautogui.write(GMAIL)
pyautogui.press('tab', presses=3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write(PASSWORD)
pyautogui.press('enter')
time.sleep(7)
pyautogui.press('tab', presses=6)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab', presses=3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab', presses=1 + NTH)
pyautogui.press('enter')
time.sleep(7)

api = TikTokApi.get_instance()
results = 10
trending = api.by_trending(count=results, custom_verifyFp="verify_kz9cm4r9_9LbXjQ6i_Stlc_4nIV_88M6_Rlp0zM9mtpx7")

# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.

for tiktok in trending:
    if tiktok['video']['duration'] < 60:
        try:
            urllib.request.urlretrieve(tiktok['video']['downloadAddr'], 'tiktokVid.mp4')
            driver.get('https://studio.youtube.com/channel/UCC_q1R0dWgpipXnt16AI58A/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D')
            time.sleep(3)
            pyautogui.press('tab', presses=3)
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.press('tab', presses=5)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write(os.path.join(os.path.realpath(__file__)[0:len(os.path.realpath(__file__))-len(sys.argv[0])-1]))
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter', presses=6)
            pyautogui.write('tiktokVid.mp4')
            pyautogui.press('tab', presses=2)
            pyautogui.press('enter')
            time.sleep(15)
            output = ''
            for i in tiktok['desc'][:98].split(' '):
                if not('#' in i) and i.replace('.', '').replace(',', '') != '':
                    output += i + ' '

            if output == '':
                output = random.shuffle(defaultTitle[0])
            pyautogui.write(output + '#fyp #shorts')
            pyautogui.press('tab', presses=2)
            pyautogui.write('Copyright {0}. {1}({2}), Tiktok all rights reserved. #tiktok #trend #trends #trending'.format(time.gmtime(tiktok['createTime']).tm_year, tiktok['author']['nickname'], tiktok['author']['uniqueId']))
            pyautogui.press('tab', presses=22)
            pyautogui.press('enter', presses=3)
            pyautogui.press('tab', presses=11)
            pyautogui.press('enter')
            time.sleep(15)
        except:
            print('an error occurred during uploading a video.')
    else:
        try:
            urllib.request.urlretrieve(tiktok['video']['downloadAddr'], 'tiktokVid.mp4')
            driver.get('https://studio.youtube.com/channel/UCC_q1R0dWgpipXnt16AI58A/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D')
            time.sleep(3)
            pyautogui.press('tab', presses=3)
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.press('tab', presses=5)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write(os.path.join(os.path.realpath(__file__)[0:len(os.path.realpath(__file__))-len(sys.argv[0])-1]))
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter', presses=6)
            pyautogui.write('tiktokVid.mp4')
            pyautogui.press('tab', presses=2)
            pyautogui.press('enter')
            time.sleep(15)
            output = ''
            for i in tiktok['desc'][:98].split(' '):
                if not('#' in i) and i.replace(',', '').replace('.', '') != '':
                    output += i + ' '

            if output == '':
                output = random.shuffle(defaultTitle[0])
            pyautogui.write('[FULL VER] ' + output + '#fyp')
            pyautogui.press('tab', presses=2)
            pyautogui.write('Copyright {0}. {1}({2}), Tiktok all rights reserved. #tiktok #trend #trends #trending'.format(time.gmtime(tiktok['createTime']).tm_year, tiktok['author']['nickname'], tiktok['author']['uniqueId']))
            pyautogui.press('tab', presses=22)
            pyautogui.press('enter', presses=3)
            pyautogui.press('tab', presses=11)
            pyautogui.press('enter')
            time.sleep(15)
        except:
            print('an error occurred during uploading a video.')

driver.quit()