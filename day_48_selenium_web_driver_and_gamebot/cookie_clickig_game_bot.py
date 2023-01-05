from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

selenium_driver_path = r"C:\Development\chromedriver.exe"

# opening browser and navigating to the url
service = Service(selenium_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# locating the cookie to click
cookie = driver.find_element(by=By.ID, value="cookie")

# locating the items in the store
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")

# getting item ids using list comprehension
item_ids = [item.get_attribute("id") for item in items]

# setting time limits to perform actions
timeout = time.time() + 5
five_min = time.time() + 300  # five minutes interval to check for items to purchase

# clicking on cookie

while True:
    cookie.click()

    # at every five seconds
    if time.time() > timeout:  # get all upgrades <b> tag
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # convert <b> price to integer
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # create a dict of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        # purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # add another 5 seconds until the next click
        timeout = time.time() + 5

        # after 5 minutes stop the bot and check the cookie per second count

        if time.time() > five_min:
            cookies_per_sec = driver.find_element(by=By.ID, value="cps").text
            print(cookies_per_sec)
            break