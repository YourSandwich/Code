from pyautogui import *
import pyautogui
import time
import keyboard
import random


time.sleep(2)

# Color of center: (255, 219, 195)


while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(2560, 240, 637, 637))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))
            yes = r + g + b
            if (b in range(0, 20)):
                pyautogui.click(x+2560, y+240)
                time.sleep(0.3)
                break
