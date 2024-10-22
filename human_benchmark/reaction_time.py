import pyautogui
import time
from pynput.mouse import Controller,Button

mouse = Controller()


def click(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)



time.sleep(2)
print("letsgo")


times_green_colour_flashed = 0


while times_green_colour_flashed < 5:
    # check if pixel at (1257, 360) is green (R value is 75)
    if pyautogui.pixel(1257, 360)[0] == 75:
        click(1257, 360)
        times_green_colour_flashed += 1
        time.sleep(1)
        click(1257, 360)
