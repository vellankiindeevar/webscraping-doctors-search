from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

ser = Service(r'C:/Users/Admin/Desktop/selenium/chromedriver.exe')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ser,options=chrome_options)

driver.get('https://stfrancismedicalcenter.com/find-a-provider/')
time.sleep(5)
url = driver.find_element(By.TAG_NAME, 'iframe').get_attribute("src")
driver.get(url)
time.sleep(5)

items = []

prev_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == prev_height:
        break
    prev_height = new_height

time.sleep(1)
element = driver.find_elements(By.CLASS_NAME, 'btnsWrapper')

for i in element:
    links = i.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        items.append(href)

# Define the filename for the JSON file
filename = "links.json"

# Write the links to the JSON file
with open(filename, "w") as f:
    json.dump(items, f,indent=4)

print(len(items))

