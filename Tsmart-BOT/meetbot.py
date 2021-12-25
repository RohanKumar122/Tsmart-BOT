from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# --------------------------------------xxxxxxxxxxxxxxxxxxxxxxxxxx-------------------------------------------
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

  # ------------------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx---------------------------------------------
chrome_browser=webdriver.Chrome(executable_path='C:\chromedriver')
chrome_browser.maximize_window()

chrome_browser.get('https://apps.google.com/intl/en-GB/meet/')

username = chrome_browser.find_element_by_xpath('//button[@class="glue-button glue-button--high-emphasis  glue-button--icon "]')
username.click()
# time.sleep(10)

# -------------------------------login----------------------------------
username = chrome_browser.find_element_by_xpath('//*[@id="identifierId"]')
username.click()
username.send_keys('elmeet@aith.ac.in')
next=chrome_browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
next.click()
time.sleep(5)


password=chrome_browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
time.sleep(2)

password.send_keys('EL@meet123')

next2=chrome_browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
next2.click()

time.sleep(25)


# ----------------------------dismiss access--------------------------------------
dismiss=chrome_browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
dismiss.click()
time.sleep(5)



# ---------------------------------Join Now-------------------------------
join =chrome_browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
join.click()

# ---------------------------------copy link------------------------------
time.sleep(8)
# tongle_for_copy_link=chrome_browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[9]/div[1]/div[1]/div/span/span/div/div[3]/i[1]')
# tongle_for_copy_link.click()
# time.sleep(2)

copy1=chrome_browser.find_element_by_xpath('//*[@id="ow3"]/div[3]/div[2]/div[3]/div[2]/button/i')
copy1.click()


















# # ----------------------------------whattsapp--------------------------

# # to_switch_tab =chrome_browser.window_handles[1]
# # chrome_browser.switch_to_window(to_switch_tab)
# time.sleep(3)
# body=chrome_browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[1]/div[1]/div/div[1]/div[3]')
# body.click()

# time.sleep(8)

# # body =chrome_browser.find_element_by_tag_name("body")
# # copy.send_keys(Keys.CONTROL + 't')
# # driver = webdriver.Chrome()
# # driver.execute_script("window.open('','_blank');")
# # chrome_browser.execute_script("window.open'https://web.whatsapp.com/','new window')")
# # new_tab = "window.open(https://web.whatsapp.com/,'_blank');"
# # new_tab.click()

# # tab_url='https://web.whatsapp.com/'
# # chrome_browser.execute_script("window.open('');")
# # chrome_browser.switch_to.window(chrome_browser.window_handles[1])
# # chrome_browser.get(tab_url)
# chrome_browser.implicitly_wait(3)
# chrome_browser.execute_script("window.open('https://web.whatsapp.com/','new window')")



# # chrome_browser.get('https://web.whatsapp.com/')
# time.sleep(15)


# user_name ='rohan3'

# user =chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
# user.click()

# message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
# message_box.send_keys(Keys.CONTROL + 'v')

# message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
# message_box.click()









