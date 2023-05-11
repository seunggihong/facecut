from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

# options = webdriver.ChromeOptions()
# #       options.add_argument('--headless')
# #       options.add_argument("--disable-extensions")
# #       options.add_argument("disable-infobars")
# #       options.add_argument("window-size=1920x1080")
#         options.add_argument("no-sandbox")
#         options.add_argument("disable-gpu")
#         options.add_argument("--lang=ko_KR")
#         options.add_argument(
#             'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

#         driver = webdriver.Chrome('크롬드라이버의 위치/chromedriver.exe', chrome_options=options)
#         driver.get('http://사이트주소')

if os.path.exists("crollimg") :
    for file in os.scandir("crollimg") :
        os.remove(file.path)

driver = webdriver.Chrome(r'/Users/ki/Desktop/python/crolling/chromedriver')
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