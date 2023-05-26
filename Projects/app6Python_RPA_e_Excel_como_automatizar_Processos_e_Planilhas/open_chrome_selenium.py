from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pyautogui as pygui

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--no-sandbox')


driver = webdriver.Chrome(service=Service('./chromedriver'),options=chrome_options)
command = open = 'www.google.com'



#pygui.sleep(4)

#driver.find_element(By.Name, "")






