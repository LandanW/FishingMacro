import os
from python_imagesearch.imagesearch import imagesearch
import win32com.client
import time
import random
import pyautogui
import cv2
import numpy as np

# create instance for sending keystroke to windows
shell = win32com.client.Dispatch("WScript.Shell")

def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    #im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc

def fish():
  timeout_start_fishing = time.time()
  number_of_fishing_rods = input("Input how many times you want to fish: ")
  caught_fish_counter = 0
  for i in range(int(number_of_fishing_rods)):
    timeout = 34
    timeout_start = time.time()
    pos = [-1,-1]
    #try to catch the fish until timeout
    while (pos[0]==-1) and (time.time()<(timeout_start+timeout)):
      pos=imagesearch("fishcaught.png")
    shell.SendKeys("e")
    if (time.time()-timeout_start)<timeout and i<(int(number_of_fishing_rods)-1):
      #print("position : ", pos[0], pos[1])
      time.sleep(6)
      time.sleep(random.randint(15,20)/10)
      caught_fish_counter += 1
      shell.sendkeys("e")
      print(f'fish caught: {caught_fish_counter}/{number_of_fishing_rods}')
    else:
      print("done!")

fish()