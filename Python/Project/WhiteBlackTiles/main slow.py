import os
import pyautogui
import keyboard
from mss.linux import MSS as mss

til_x = [2625, 2790, 2950, 3100]
til_y = [805, 640, 480, 320]

while keyboard.is_pressed('q') == False:
    for x in til_x:
        for y in til_y:
            if pyautogui.pixel(x, y)[0] == 0:
                pyautogui.click(x, y)
                break
