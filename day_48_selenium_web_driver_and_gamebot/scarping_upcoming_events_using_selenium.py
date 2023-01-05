from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

selenium_driver_path = r"C:\Development\chromedriver.exe"

service = Service(selenium_driver_path)  # setting up Service object with selenium chrome driver path
driver = webdriver.Chrome(service=service)  # creating driver to automate web tasks

# Interacting with wikipedia website:

driver.get("https://www.python.org/")  # url to target webpage

# Scraping for upcoming events on this webpage----------------------------------------------------------

upcoming_events = {}  # we need the time and name of events as a key value pair in a dictionary

event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
for time in event_times:
    print(time.text)

event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget ul li a")
for name in event_names:
    print(name.text)

# combining times and event names into a nested dictionary using dictionary comprehension

upcoming_events = {i: {"Time": event_times[i].text, "Event Name": event_names[i].text} for i in range(len(event_names))}
print(upcoming_events)
driver.quit()

