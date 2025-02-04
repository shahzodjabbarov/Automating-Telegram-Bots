import pyautogui
from PIL import ImageGrab  # To capture the screen and get pixel colors
import time
# Specify the coordinates for which we want RGB values
time.sleep(5)

def check():
    coor = []
    left = [(654, 448), (654, 341), (654, 230)]
    right = [(787, 448),(787, 341), (787, 230)]
    colors = [(133, 57, 20, 255), (176, 89, 13, 255), (142, 53, 6, 255), (130, 50, 5, 255), (142, 53, 7, 255) , (221, 133, 69, 255), (142, 54, 7, 255), (176, 89, 13, 255), (170, 83, 12, 255), (130, 50, 5, 255), (169, 83, 12, 255), (149, 65, 8, 255), (135, 53, 6, 255), (156, 71, 9, 255),  (176, 89, 13, 255),(221, 133, 69, 255), (142, 54, 7, 255),(139, 57, 7, 255), (170, 83, 12, 255)]
    screen = ImageGrab.grab()
    
    for i in range(3):

        colorl = screen.getpixel(left[i])
        print("Left ", i+1, ":", colorl, {colorl in colors})

        colorr = screen.getpixel(right[i])
        print("Right ", i+1, ":", colorr, {colorr in colors})
        if colorl in colors:
            coor.append(1)
        elif colorr in colors:
            coor.append(0)
        else:
            coor.append(1)
            

    print(coor)
    hitplan(coor)



def sixhit(coor):
    global first
    first = False

    for i in coor:
        if i == 0:
            pyautogui.click(600, 550)
            time.sleep(0.025)
            pyautogui.click(600, 550)
            time.sleep(0.025)

        elif i == 1:
            pyautogui.click(800, 550)
            time.sleep(0.025)
            pyautogui.click(800, 550)
            time.sleep(0.025)

        else:
            print("None found")

    time.sleep(0.6)
    check()

first = True
last = None

def hitplan(coor):
    global first
    global last


    if first:
        last = coor[2]
        coor.insert(0, 0)
        coor.pop()
        print("Going to sixhit: ", coor)
        sixhit(coor)

    
    else:
        coor.insert(0, last)
        last = coor[3]
        coor.pop()
        print("Going to sixhit: ", coor)
        sixhit(coor)

check()
