from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

selenium_driver_path = r"C:\Development\chromedriver.exe"

# setting up Service and driver to open the browser
service = Service(selenium_driver_path)
driver = webdriver.Chrome(service=service)

# navigating to the url
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.click()
first_name.send_keys("test")
# first_name.send_keys(Keys.ENTER)

last_name = driver.find_element(by=By.NAME, value="lName")
# last_name.click()
last_name.send_keys("test")
# last_name.send_keys(Keys.ENTER)

email = driver.find_element(by=By.NAME, value="email")
# email.click()
email.send_keys("testtest@email.com")
# email.send_keys(Keys.ENTER)

# sign_up_btn = driver.find_element(by=By.CLASS_NAME, value="btn")
sign_up_btn = driver.find_element(by=By.CSS_SELECTOR, value="form button")
sign_up_btn.click()
