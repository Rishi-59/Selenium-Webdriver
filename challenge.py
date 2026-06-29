from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    'detach',
    True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

fName = driver.find_element(By.NAME, 'fName')
lName = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
btn = driver.find_element(By.TAG_NAME, 'button')

fName.send_keys("Kunal", Keys.ENTER)
lName.send_keys("More", Keys.ENTER)
email.send_keys("om@pandit.com", Keys.ENTER)
btn.click()