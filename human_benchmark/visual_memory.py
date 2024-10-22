import time
import pyautogui
from pynput.mouse import Controller,Button

mouse = Controller()


def click(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)


limit = 50
image = None

click(954, 558)
time.sleep(1)

for _ in range(limit):

    image = pyautogui.screenshot(region=(750, 259, 400, 400))

    time.sleep(1.1)

    for i in range(0, 400, 20):
        for j in range(0, 400, 20):
            if image.getpixel((i, j)) == (255, 255, 255):  # gets the colour of the pixel
                click(i + 750, j + 259)

    time.sleep(2)
