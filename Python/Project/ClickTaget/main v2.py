import pyautogui
import time
import mouse
from mss import mss

width, height = (600, 400)
bbox = (2581, 338, 2581 + width, 338 + height)
# Color of center: (255, 219, 195)

with mss() as sct:
    while True:
        img = sct.grab(bbox)
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r = img.pixel(x, y)[0]
                g = img.pixel(x, y)[1]
                b = img.pixel(x, y)[2]
                if r == 255:
                    if g == 219:
                        if b == 195:
                            mouse.move(x+2581, y+338)
                            pyautogui.click()
                            time.sleep(0.005)
                            break
