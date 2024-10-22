import time

import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

start_button = 'esc'

stop_browser = 'b'

# set up Selenium browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://humanbenchmark.com/tests/verbal-memory")

keyboard.wait(start_button)

seen_button = browser.find_element(By.XPATH, '//button[text()="SEEN"]')
new_button = browser.find_element(By.XPATH, '//button[text()="NEW"]')

# store seen words
words = set()

while not keyboard.is_pressed("q"):

    word = browser.find_element(By.CLASS_NAME, 'word').text

    if word in words:
        seen_button.click()
    else:
        new_button.click()
        words.add(word)
    time.sleep(0.01)

keyboard.wait(stop_browser)
print("finished :3")
