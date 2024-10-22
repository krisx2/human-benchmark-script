import time

import keyboard
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

start_button = 'esc'
stop_browser = 'b'
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://humanbenchmark.com/tests/number-memory")
keyboard.wait(start_button)
flag = False
while not keyboard.is_pressed("q"):

    try:

        elements = browser.find_element(By.CLASS_NAME, "big-number")
        current_number = elements.text
        submit_button = None

        while not submit_button:
            if keyboard.is_pressed("q"):
                flag = True
                break
            try:

                submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
                end_time = time.perf_counter()
            except NoSuchElementException:
                print("Waiting for animation....")
                time.sleep(0.5)
        if flag:
            break
        keyboard.write(current_number)
        submit_button.click()
        time.sleep(0.2)
        next_button = browser.find_element(By.XPATH, '//button[text()="NEXT"]')
        next_button.click()


    except NoSuchElementException:
        print("Not found.... Start game pls")
        time.sleep(0.5)
print("stopped loop")
keyboard.wait(stop_browser)
