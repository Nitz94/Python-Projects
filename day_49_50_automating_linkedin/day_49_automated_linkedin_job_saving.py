#  AUTOMATING LINKEDIN FOR EASIER JOB APPLICATIONS:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException  # to handle exception
import time


# setting up selenium chrome driver path

selenium_web_driver = r"C:\Development\chromedriver.exe"

# setting up driver and service to open the browser
service = Service(selenium_web_driver)
driver = webdriver.Chrome(service=service)

# navigating to the url
driver.get(r"https://www.linkedin.com/jobs/search/?currentJobId=3312246521&geoId=109045472&keywords="
           r"Python%20Developer&location=Thiruvananthapuram%2C%20Kerala%2C%20India&refresh=true")

# going to sign in page
sign_in_link = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in_link.click()
time.sleep(3)

# filling signin page
user_name = driver.find_element(by=By.ID, value="username")
user_name.click()
user_name.send_keys("USER NAME")

password = driver.find_element(by=By.ID, value="password")
password.click()
password.send_keys("PASSWORD")

submit_button = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
submit_button.click()
time.sleep(5)

# saving first few listed jobs

for i in range(1, 5):
    job_listing = driver.find_elements(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]")
    job_listing.click()
    time.sleep(3)
    # saving

    save = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
    save.click()





