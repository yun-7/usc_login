from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
import time

driver = webdriver.Chrome()
driver.get('https://ap.usc.edu.tw/SSO/login.aspx?ReturnUrl=/sso/')
# 開啟首頁
account = driver.find_element(By.ID, 'txtMyId')
account.send_keys('A110280082')
password = driver.find_element(By.ID, 'txtMyPd')
password.send_keys('YOUR_PASSWORD')

time.sleep(2)
ocr = ddddocr.DdddOcr()
captcha_img = driver.find_element(By.ID, 'Img_Valid')
captcha_img.screenshot('code.png')
with open('code.png', 'rb') as fp:
    img = fp.read()
result = ocr.classification(img)

valid = driver.find_element(By.ID, 'tdValidCode')
valid.send_keys(result)

login = driver.find_element(By.ID, 'btnLogin')
login.click()
