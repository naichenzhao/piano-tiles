'''
    So, this is the code
    The actual piano tiles game can be accessed here: http://tanksw.com/piano-tiles/
        Remember to have it on full screen on the macbook pro window while running windows

    TODO: Probably add multiple layers of clicking to make it go for longer
        I can also probably decrease the area that i take the screenshot

'''

import time
from PIL import ImageGrab
import win32api, win32con


# |---------------------| Defining the 'click' function |---------------------|

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


# |---------------------| Initiating the variables |---------------------|

im = ImageGrab.grab([1190, 1260, 1723, 1264])

A1 = im.getpixel((0, 0))
A2 = im.getpixel((0, 3))

S1 = im.getpixel((177, 0))
S2 = im.getpixel((177, 3))

D1 = im.getpixel((354, 0))
D2 = im.getpixel((354, 3))

F1 = im.getpixel((531, 0))
F2 = im.getpixel((531, 3))


time.sleep(1)
print("ready")


# |---------------------| Main loop |---------------------|

while(True):




    im = ImageGrab.grab([1190, 1180, 1723, 1264])

    A1 = im.getpixel((0, 80))
    A2 = im.getpixel((0, 83))

    S1 = im.getpixel((177, 80))
    S2 = im.getpixel((177, 83))

    D1 = im.getpixel((354, 80))
    D2 = im.getpixel((354, 83))

    F1 = im.getpixel((531, 80))
    F2 = im.getpixel((531, 83))

    if A1 < (20, 20, 20) and A2 < (20, 20, 20):
        click(700, 860)
    elif S1 < (20, 20, 20) and S2 < (20, 20, 20):
        click(800, 860)
    elif D1 < (20, 20, 20) and D2 < (20, 20, 20):
        click(900, 860)
    elif F1 < (20, 20, 20) and F2 < (20, 20, 20):
        click(1000, 860)
