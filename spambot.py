import pyautogui
import time
time.sleep(5)

f = open("script", 'r')

for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")



