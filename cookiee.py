
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

print('Looking for Language button...')

try:
    lang = driver.find_element(By.ID, 'langSelect-EN')
    print('Language button found')
    lang.click()
    sleep(3)
    got_it = driver.find_element(By.CLASS_NAME, 'cc_btn.cc_btn_accept_all')
    print('Clicked accept all button')
    got_it.click()
    sleep(3)
except NoSuchElementException:
    print("No language selection found")

sleep(2)

cookie = driver.find_element(By.ID,'bigCookie')

item_ids = [f'product{i}' for i in range(1,20)]

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

def cal_min_price(min_price = float('inf')):
    for product in products:
        price = int(product.find_element(By.CLASS_NAME, 'price').text.replace(',', ''))
        print(f'price: {price}')
        if min_price > price:
            min_price = int(price)
    return int(min_price)

def get_cookie_count():
    cookie_count_tag = driver.find_element(By.ID, 'cookies')
    cookie_count = cookie_count_tag.text.split()[0]
    cookie_count = int(cookie_count.replace(',', ''))
    print(f'cookie_count: {cookie_count}')
    return cookie_count

def get_available_products():
    return driver.find_elements(By.CLASS_NAME, 'product.unlocked.enabled')

def get_available_upgrades():
    return driver.find_elements(By.CLASS_NAME, 'crate.upgrade.enabled')

def get_best_product():
    if products:
        best_product = products[-1]
        print(f'Best product: {best_product.text}')
        return best_product
    else:
        return None

def get_best_upgrade():
    best_upgrade = upgrades[0]
    print(f'Best upgrade: {best_upgrade.get_attribute("id")}')
    return best_upgrade

print("Starting game..")
while True:
    try:
        cookie.click()

        if time() > timeout:
            print('Timed out Choosing Upgrades')
            current_cookie_count = get_cookie_count()

            products = get_available_products()
            print(f'Available products: {len(products)}')

            upgrades = get_available_upgrades()
            print(f'Available upgrades: {len(upgrades)}')

            current_best_upgrade = None
            current_best_product = None
            current_min_product_price = float('inf')

            if upgrades:
                current_best_upgrade = get_best_upgrade()
                current_best_upgrade.click()
                current_cookie_count = get_cookie_count()

            if products:
                current_best_product = get_best_product()
                current_min_product_price = cal_min_price()

            while current_min_product_price < current_cookie_count and products and current_best_product:
                print(f'Current min_price: {current_min_product_price}')

                best_product_price = int(current_best_product.find_element(By.CLASS_NAME, 'price').text.replace(',', ''))
                print(f'Best product price: {best_product_price}')

                current_best_product = get_best_product()

                if current_best_product:
                    current_best_product.click()

                current_cookie_count = get_cookie_count()

                current_min_product_price = cal_min_price()

                products = get_available_products()

            timeout = time() + wait_time

        if time() > five_min:
            print('*' * 50)
            print('\n\nTime is up ...')
            cookies_per_sec = driver.find_element(By.ID, 'cookiesPerSecond').text.split()[-1]
            print(f'Cookies per second: {cookies_per_sec}')
            break

    except ElementClickInterceptedException:
        sleep(1)
        pass
