import time
import pyautogui
from pynput.mouse import Controller,Button

mouse = Controller()
def click(x,y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)


targets_hit = 0  # keeps track of how many targets are clicked
time.sleep(2)
print("go")

# initial click to start the process
click(950, 430)

# loop runs until all targets are clicked
while targets_hit < 31:

    # take a screenshot of the specified region
    pic = pyautogui.screenshot(region=(463, 231, 900, 460))
    width, height = pic.size
    flag = False  # used to break the loops when a target is found

    # iterate over the screenshot height and width with steps of 20 pixels
    for w in range(0, width, 20):
        for h in range(0, height, 20):

            # get the RGB value of the pixel
            r, g, b = pic.getpixel((w, h))

            # check if the pixel matches the target colors (white or light blue)
            if (r, g, b) == (255, 255, 255) or (r, g, b) == (149, 195, 232):

                click(w + 463, h + 231)

                targets_hit += 1
                flag = True
                time.sleep(0.01)  # short delay after each click to prevent double-clicking

                break
        if flag:
            break
