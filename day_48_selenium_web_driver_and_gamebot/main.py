from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

selenium_driver_path = r"C:\Development\chromedriver.exe"  # chrome driver path


# DEPRECATED METHOD
# ______________________________________________________________________________________________________
# driver = webdriver.Chrome(executable_path=selenium_driver_path)  # setting selenium for chrome
#
# # driver.get("https://www.amazon.in/")  # opens up the webpage
#
# # driver.close()  # closes the current tab
# # driver.quit()  # closes the entire browser
# driver.get("https://www.amazon.in/Samsung-Galaxy-Phantom-Storage-Watch4/dp/"
#            "B09SH994JW/ref=sr_1_1_sspa?crid=U902R2YT1B6M&keywords=samsung%2Bgalaxy%2Bs22%"
#            "2Bultra&qid=1664646935&qu=eyJxc2MiOiI0LjQ4IiwicXNhIjoiNC4yNCIsInFzcCI6IjEuNTkifQ%3D%"
#            "3D&sprefix=samsung%2Bgalaxy%2Bs22%2Caps%2C376&sr=8-1-spons&th=1")
#
# price = driver.find_element_by_id()
# # print(price.text)
# ______________________________________________________________________________________________________________

service = Service(selenium_driver_path)   # creating a service object
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
price = driver.find_element(by=By.CLASS_NAME, value="introduction")
# print(price.text)

search_bar = driver.find_element(by=By.NAME,value="q" )
print(search_bar.get_attribute("placeholder"))  # prints selenium object if just variable is given

logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(logo.size)

documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".small-widget.documentation-widget p a")
# class="small-widget documentation-widget" dot for css selector
print(documentation_link.get_attribute("href"))

bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)  # x link is obtained from browser. used incase if identification of elements is too difficult

# close the current tab
driver.close()

# close the entire browser
driver.quit()
