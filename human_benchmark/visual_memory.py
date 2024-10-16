import time

import pyautogui
from win32api import mouse_event, SetCursorPos
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP


def click(x, y):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)


limit = 50

image = None

click(954, 558)
time.sleep(1)


for x in range(0, limit):

    image = pyautogui.screenshot(region=(750, 259, 400, 400))

    time.sleep(1.1)

    for i in range(0, 400, 20):
        for j in range(0, 400, 20):
            if image.getpixel((i, j)) == (255, 255, 255):
                click(i + 750, j + 259)

    time.sleep(2)
