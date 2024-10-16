import sys
import pyautogui
import keyboard
import time
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from win32api import mouse_event, SetCursorPos



def click(x, y):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)


# delay for setup
time.sleep(3)
print("letsgo")

count_of_squares = 1  # tracks the number of tiles to process
tiles_lit = []  # stores the coordinates of detected tiles

# initial click to start the game
click(954, 570)

# main loop runs until 'q' is pressed
while not keyboard.is_pressed('q'):

    # list of target tile positions (3x3 grid)
    positions = [(816, 333), (950, 333), (1085, 333),
                 (816, 464), (950, 464), (1085, 464),
                 (816, 600), (950, 600), (1085, 600)]

    # loop runs until the required number of tiles are detected
    while len(tiles_lit) < count_of_squares:
        if keyboard.is_pressed("q"):
            sys.exit()

        # check each position for white pixels (255) and store the positions
        for pos in positions:
            if pyautogui.pixel(pos[0], pos[1])[0] == 255:
                tiles_lit.append(pos)

        # small delay to avoid double counting the same lit tile
        time.sleep(0.45)

    # click the detected tiles and increase the count for next round
    if tiles_lit:
        count_of_squares += 1
        for pos in tiles_lit:
            click(*pos)

    # clear the list of tiles after clicking and delay before the next round
    tiles_lit.clear()
    time.sleep(0.6)
