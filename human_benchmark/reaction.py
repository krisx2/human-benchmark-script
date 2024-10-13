import pyautogui
import time
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from win32api import mouse_event, SetCursorPos


def click(x, y):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

# delay for setup
time.sleep(2)
print("letsgo")


times_green_colour_flashed = 0 # times the green color flashed


while times_green_colour_flashed < 5:
    # check if pixel at (1257, 360) is green (R value is 75)
    if pyautogui.pixel(1257, 360)[0] == 75:
        click(1257, 360)  # click on the detected green pixel
        times_green_colour_flashed += 1
        time.sleep(1)  # delay before the next check
        click(1257, 360)  # click again after the delay to keep the test going
