import pyautogui
from mss import mss

start_x = 2560
start_y = 240

bbox = (start_x, start_y, start_x + 637, start_y + 637)

cords_x = (0, 200, 400, 600)


def start():
    with mss() as sct:
        t = 0
        cordy = 0
        while True:
            img = sct.grab(bbox)
            for cordx in cords_x:
                if img.pixel(cordx, cordy)[0] <= 23:
                    pyautogui.click(start_x + cordx, start_y + cordy)
                    break
            if t == 4:
                cordy += 200
            else:
                if t == 8:
                    cordy += 200
                else:
                    if t == 12:
                        cordy += 200
                    else:
                        if t == 16:
                            cordy -= 600
                            t -= 16

            t += 1


start()
