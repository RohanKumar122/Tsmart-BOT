from selenium import webdriver
import time
import pyperclip
import pyautogui as P

chrome_browser=webdriver.Chrome(executable_path='D:\chromedriver')
chrome_browser.maximize_window()


# ---------------------------whattsapp--------------------------------------------
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(18)

user_name ='My'

user =chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()
time.sleep(5)

message_box  = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
time.sleep(1)
message_box.send_keys('This is the link for DSP')
time.sleep(1)
message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
message_box.click()
time.sleep(1)
message_box  = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
message_box.send_keys("")
P.hotkey("ctrl","v")
message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
message_box.click()
time.sleep(2)
message_box  = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
message_box.send_keys('Join Sharp at 10:00 am.')
message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
message_box.click()
time.sleep(2)

















