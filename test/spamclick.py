import pyautogui
import time

time.sleep(1)

start_x = pyautogui.position()[0]
start_y = pyautogui.position()[1]
for i in range(0, 1000):
    pyautogui.click(start_x, start_y)
