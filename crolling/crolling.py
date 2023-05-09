import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

driver = webdriver.Chrome(r'/Users/ki/Desktop/crolling/chromedriver')
# url
driver.get("https://images.google.com/")
elem = driver.find_element_by_name('q')
# search
elem.send_keys("강호동")
elem.send_keys(Keys.RETURN)

scroll_cnt = 3
last_height = driver.execute_script("return document.body.scrollHeight")
while scroll_cnt != 0 :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height :
        try :
            driver.find_element_by_css_selector(".mye4qd").click()
        except :
            break
    last_height = new_height
    scroll_cnt -= 1

imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for img in imgs :
    img.click()
    time.sleep(2)
    imgUrl = driver.find_element_by_css_selector(".r48jcc").get_attribute("src")
    urllib.request.urlretrieve(imgUrl,"crollimg/{}.jpg".format(count))
    count += 1

driver.close()