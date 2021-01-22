from pyautogui import *
import pyautogui
import time
import keyboard
import random


time.sleep(2)

# Color of center: (255, 219, 195)


while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(2581, 338, 600, 400))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))
            yes = r + g + b
            if b == 195:
                pyautogui.click(x+2581, y+338)
                time.sleep(0.3)
                break
