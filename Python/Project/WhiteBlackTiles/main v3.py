import pyautogui
import keyboard
from mss import mss

start_x = 2560
start_y = 240

bbox = (start_x, start_y, start_x + 637, start_y + 637)


def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            width, height = img.size
            for x in range(0, width, 20):
                for y in range(0, height, 20):
                    if img.pixel(x, y)[0, 1, 2] == (0, 0, 0):
                        pyautogui.click(x + start_x, y + start_y)
                        break


start()
