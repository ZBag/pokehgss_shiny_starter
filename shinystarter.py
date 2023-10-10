import keyboard
import pyautogui
import time
import cv2
import numpy as np
import imutils
from PIL import Image, ImageChops

total = 0
found = False
chik = cv2.imread("pic/c1.png")
toto = cv2.imread("pic/t1.png")
cy = cv2.imread("pic/cy1.png")
def pt(k):
    pyautogui.keyDown(k)
    pyautogui.keyUp(k)
    return None

def start_state():
    global total
    pt("f")
    total += 1
    while (pyautogui.locateOnScreen("pic/new_game_button.png") == None):
        pt("p")
        time.sleep(0.5)
    time.sleep(0.5)
    pt("p")
    time.sleep(0.5)
    pt("p")
    time.sleep(0.5)
    pt("p")
    time.sleep(0.5)
    return shiny_pokemon()



def shiny_pokemon():
    global found
    for a in range(3):
        if (found == True):
            print("found something different")
            return None
        time.sleep(0.25)
        #390, 635, 565, 450
        #take screenshot
        sc = pyautogui.screenshot()
        sc = np.array(sc)
        sc = cv2.cvtColor(sc, cv2.COLOR_RGB2BGR)

        #crops the screenshot
        cc = sc[450:635, 390:565]

        #print(cc.shape)
        #print(cy.shape)
        #cv2.imshow('Screenshot', cc)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        #find difference between images
        check1 = cv2.absdiff(cy, cc)
        check2 = cv2.absdiff(chik, cc)
        check3 = cv2.absdiff(toto, cc)
        if ((np.sum(check1) == 0) | (np.sum(check2) == 0) | (np.sum(check3) == 0)):
            pt("a")
            time.sleep(0.25)
        else:
            found = True
            return print("Found something different")
    if (found == True):
        return print("Last time caught it..")
    else:
        return print("Nothing found resetting #"+str(total))

keyboard.wait('g')
while found == False:
    start_state()
keyboard.wait('h')