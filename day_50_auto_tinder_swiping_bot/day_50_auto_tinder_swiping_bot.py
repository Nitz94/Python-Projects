import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# selenium chrome driver path
selenium_web_driver_path = r"C:\Development\chromedriver.exe"

# Setting up driver and service

service = Service(selenium_web_driver_path)
driver = webdriver.Chrome(service=service)

# NOTE THAT THE TINDER CHANGES THE WEBSITE FREQUENTLY SO ELEMENT VALUES MIGHT CHANGE.
# navigating to tinder log in page

driver.get("https://tinder.com/")
time.sleep(3)

log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="q-1380955487"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in_button.click()
time.sleep(3)

# clicking on log in with facebook from the list
try:
    login_with_fb = driver.find_element(by=By.XPATH, value='//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
    login_with_fb.click()

except NoSuchElementException:  # if pop up does not have that button, click on more options to log in
    time.sleep(3)
    more_options_to_log_in = driver.find_element(by=By.XPATH, value='//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/button')
    more_options_to_log_in.click()
    time.sleep(2)
    login_with_fb = driver.find_element(by=By.XPATH, value='//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
    login_with_fb.click()
    time.sleep(10)

# selenium has unique window handles for each window. can be returned as a list. base window is at index 0
# print(driver.window_handles)


# new window now popped up
base_window = driver.window_handles[0]
fb_log_in_window = driver.window_handles[1]

# switching to thw new window
driver.switch_to.window(fb_log_in_window)
print(driver.title)  # checking the title to be sure. returns facebook as title

# filling facebook login form
email_address = "EMAIL ADDRESS"
password = "PASSWORD"

email_ad_fb = driver.find_element(by=By.ID,value='email')
email_ad_fb.click()
email_ad_fb.send_keys(email_address)
pass_fb = driver.find_element(by=By.ID,value='pass')
pass_fb.click()
pass_fb.send_keys(password)

log_in_fb = driver.find_element(by=By.NAME, value="login")
log_in_fb.click()
time.sleep(15)

# switching back to base window and dismissing all popups when signing in, allowing location and cookies
driver.switch_to.window(base_window)
location_pop_up = driver.find_element(by=By.XPATH, value='//*[@id="t-275949266"]/main/div/div/div/div[3]/button[1]/span')
location_pop_up.click()
time.sleep(3)
# disabling notification
notification_pop_up = driver.find_element(by=By.XPATH, value='//*[@id="t-275949266"]/main/div/div/div/div[3]/button[2]/span')
notification_pop_up.click()
time.sleep(3)
cookie_pop_up = driver.find_element(by=By.XPATH, value='//*[@id="t1452431810"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookie_pop_up.click()

# hitting likes on profile:
# tinder free tire only allows 100 likes per day

for n in range(100):

    # add a 1-second delay between likes
    time.sleep(2)

    try:
        # print("called")
        like_button = driver.find_element(by=By.XPATH, value='//*[@id="t1452431810"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span/svg/path')
        like_button.click()
        time.sleep(2)

    # catches the case where there is a matched pop-up in front of the like button
    except ElementClickInterceptedException:
        match_popup = driver.find_element(by=By.ID, value='q1673317088')
        match_popup.send_keys("Beep-Boop-Beep_I am a Bot")
        match_popup = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/div[3]/form/button')
        match_popup.click()
        time.sleep(1)
    except NoSuchElementException:  # if tinder add to home popup
        try:
            not_interested = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button[2]')
            not_interested.click()
            time.sleep(1)
        except NoSuchElementException:  # if upgrade to premium pops up

            no_thanks = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[3]/button[2]')
            no_thanks.click()
            time.sleep(1)
    #

driver.close()
