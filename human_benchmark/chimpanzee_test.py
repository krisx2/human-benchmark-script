import time

import keyboard
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

stop_browser = "b"
start_button = 'esc'
number_count = 4
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://humanbenchmark.com/tests/chimp")
keyboard.wait(start_button)

while not keyboard.is_pressed("q") and number_count < 41:
    for i in range(1, number_count + 1):
        try:
            element = browser.find_element(By.XPATH, f'//div[@data-cellnumber="{i}"]')
            element.click()
        except NoSuchElementException:
            break
    try:
        continue_button = browser.find_element(By.XPATH, '//button[text()="Continue"]')
        continue_button.click()
        time.sleep(0.1)
        number_count += 1
    except NoSuchElementException:
        break
print("stopped loop")
keyboard.wait(stop_browser)
