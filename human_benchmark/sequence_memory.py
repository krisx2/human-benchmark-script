import time
import keyboard
import pyautogui
from pynput.mouse import Controller,Button

mouse = Controller()


def click(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)


time.sleep(3)
print("letsgo")

count_of_squares = 1
tiles_lit = []

click(954, 570)

while not keyboard.is_pressed('q'):

    # list of target tile positions (3x3 grid)
    positions = [(816, 333), (950, 333), (1085, 333),
                 (816, 464), (950, 464), (1085, 464),
                 (816, 600), (950, 600), (1085, 600)]

    # loop runs until the required number of tiles are detected
    while len(tiles_lit) < count_of_squares:
        if keyboard.is_pressed("q"):
            break

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

    tiles_lit.clear()
    time.sleep(0.6)
