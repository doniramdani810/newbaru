import threading
import pyautogui
from PIL import ImageGrab
import keyboard
import os
import time
import cv2
import numpy as np
import glob
import pytesseract
import mss

path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\CROT\crot\*.png"
files = glob.glob(path)

def process_file(file):
    template = cv2.imread(file, 0)

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Set the similarity level (0-1)
    similarity = 0.7

    # Check if the template is on the screen
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= similarity)

    if len(loc[0]) > 0:
        # Get the center of the first match
        x, y = loc[1][0], loc[0][0]
        w, h = template.shape[1], template.shape[0]
        center = (x + w/2, y + h/2)

        # Click at the center
        original_position = pyautogui.position()
        pyautogui.click(center)
        pyautogui.moveTo(original_position)
        time.sleep(1)

while True:
    for file in files:
        threading.Thread(target=process_file, args=(file,)).start()
