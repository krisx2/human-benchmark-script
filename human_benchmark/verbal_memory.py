import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
from selenium.webdriver.chrome.service import Service

start_button = 'p'
end_button = "o"
stop_browser = 'b'

# set up Selenium browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://humanbenchmark.com/tests/verbal-memory")


keyboard.wait(start_button)


seen_button = browser.find_element(By.XPATH, '//button[text()="SEEN"]')
new_button = browser.find_element(By.XPATH, '//button[text()="NEW"]')

# store seen words
words = set()

while True:

    word = browser.find_element(By.CLASS_NAME, 'word').text

    if word in words:
        seen_button.click()
    else:
        new_button.click()
        words.add(word)
    time.sleep(0.01)

    if keyboard.is_pressed(end_button): break


keyboard.wait(stop_browser)