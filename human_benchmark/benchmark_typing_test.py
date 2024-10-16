import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

start_button = 'esc'
stop_browser = 'b'

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://humanbenchmark.com/tests/typing")

keyboard.wait(start_button)

elements = browser.find_elements(By.CLASS_NAME, "incomplete")

text = ""
for element in elements:
    element_text = element.text
    text += element_text if len(element_text) > 0 else ' '


keyboard.write(text)

keyboard.wait(stop_browser)
