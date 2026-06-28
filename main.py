from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach' , True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

data = {}
index = 0
for event in events:
    date = event.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]
    name = event.find_element(By.TAG_NAME, "a").text

    data[index] = {'date' : date, 'name' : name}
    index += 1
    
pprint(data)
driver.quit()