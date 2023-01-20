import os
import threading
import pyautogui

# Define the target RGB values
target_rgb = (255, 219, 195)

def find_and_click():
  # Get the current mouse position
  current_position = pyautogui.position()

  # Get the RGB values at the current mouse position
  current_rgb = pyautogui.pixel(*current_position)

  # Compare the current RGB values to the target RGB values
  if current_rgb == target_rgb:
    # If they match, left-click on the pixel
    pyautogui.click(button='left')

# Create a thread for each CPU core on the system
threads = [threading.Thread(target=find_and_click) for _ in range(os.cpu_count())]

# Start all threads
for thread in threads:
  thread.start()

# Wait for all threads to finish
for thread in threads:
  thread.join()
