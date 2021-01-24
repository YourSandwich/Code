import pyautogui
from mss import mss

start_x = 2690
start_y = 727

bbox = (start_x, start_y, start_x + 350, start_y + 100)

cords_x = (0, 120, 240, 349)


def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            for cordx in cords_x:
                if img.pixel(cordx, 0)[0] <= 0:
                    pyautogui.moveTo(start_x + cordx, start_y)
                    pyautogui.click()
                    break


start()
