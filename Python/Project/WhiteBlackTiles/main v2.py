import pyautogui
import keyboard
import mouse
from mss import mss

start_x = 2560
start_y = 240

bbox = (start_x, start_y, start_x + 637, start_y + 637)


def start():
    with mss() as sct:
        while keyboard.is_pressed('q') == False:
            while True:
                img = sct.grab(bbox)
                width, height = img.size
                for x in range(0, width, 20):
                    for y in range(0, height, 20):
                        if img.pixel(x, y)[0] == 20:
                            mouse.move(x + start_x, y + start_y, absolute=True,
                                       duration=0)
                            pyautogui.click()
                            break


start()
