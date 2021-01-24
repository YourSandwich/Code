import pyautogui
import time
import mouse
import random


time.sleep(2)

# Color of center: (255, 219, 195)


while True:

    pic = pyautogui.screenshot(region=(2581, 338, 600, 400))

    width, height = pic.size
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))
            if r == 255:
                if g == 219:
                    if b == 195:
                        mouse.move(x+2581, y+338)
                        mouse.click('left')
                        pyautogui.click()
                        time.sleep(0.08)
                        break
