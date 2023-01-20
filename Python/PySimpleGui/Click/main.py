import pyautogui
import threading
from keyboard import is_pressed

THREAD_LIMIT = 10  # The maximum number of threads to create

def find_and_click_image():
    # Search the screen for an image that is similar to example.jpg
    # This will return the coordinates of the top-left corner of the image
    image_coords = pyautogui.locateOnScreen('exa.png')

    # If no image was found, skip the rest of the function
    if image_coords is None:
        return

    # Calculate the coordinates of the center of the image
    center_x = image_coords[0] + (image_coords[2] / 2)
    center_y = image_coords[1] + (image_coords[3] / 2)

    # Move the mouse to the center of the image and click
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click()

# Start the thread and run in a loop until the user presses the Escape key
while not is_pressed('esc'):
    # Check the number of active threads
    if threading.active_count() < THREAD_LIMIT:
        # Create a new thread to search for the image and click on it
        thread = Thread(target=find_and_click_image)

        # Start the thread
        thread.start()
