# Python & Selenium Chrome Webdriver 
# Gmail login Automation 
# Created on 21.02.2018 
# Created by vukasiN. 

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Username
user = "youremail@gmail.com"

# Password
pwd = "yourpassword"

# Chrome Driver
driverpath = "selenium/webdriver/chrome/chromedriver.exe" # put your path to chromedriver 

# Open Chrome
driver = webdriver.Chrome(driverpath)
driver.maximize_window()

# Open Gmail Page
driver.get("http://www.gmail.com")
time.sleep(2)

# Input Username or Email
element = driver.find_element_by_id("identifierId")
element.send_keys(user)
time.sleep(1)

# Press next for password
next = driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
time.sleep(1)

# Enter Password
element = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
element.send_keys(pwd)
time.sleep(1)

# Login Button
driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
time.sleep(5)

# Close Browser
driver.close()