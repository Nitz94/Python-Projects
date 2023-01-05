from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # used to send keys which are not texts

selenium_driver_path = r"C:\Development\chromedriver.exe"

# setting up service and driver
service = Service(selenium_driver_path)
driver = webdriver.Chrome(service=service)

# Interacting with wikipedia website___________________________________________________________

driver.get("https://en.wikipedia.org/wiki/Main_Page")   # wikipedia url
#
#
# # using css selectors and nth child method
# # total_number_of_articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount > a:nth-child(1)")
# # print(total_number_of_articles.text)  # printing only the article count
#
#
# # using css selector. # for id and . for class
article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
#
# Clicking on a link: just call click method
# article_count.click()

# Clicking on links once you identify them by giving link text
# provide the actual link text from the webpage to find the element and use click method on it
content_portal = driver.find_element(by=By.LINK_TEXT, value="Content portals")
# content_portal.click()


# Typing text into a website
search_box = driver.find_element(by=By.NAME, value="search")  # finding the element
# for typing text use send keys method
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)

driver.quit()
# ______________________________________________________________________________________________________

