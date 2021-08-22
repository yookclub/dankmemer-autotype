import pynput
import random
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
i = 0

while i < 1:
    
    keyboard.type('pls hunt')
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type('pls fish')
    keyboard.press(Key.enter)
    time.sleep(3)
    time.sleep(4)
    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type('pls dig')
    keyboard.press(Key.enter)
    time.sleep(2)
    time.sleep(49)

