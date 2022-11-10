import pyautogui as py
import time

message = "teste"
count = 1

time.sleep(2)

for i in range(10):
  py.typewrite(message + " " + str(count))
  py.press('Enter')
  count = count + 1