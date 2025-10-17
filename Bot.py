import pyautogui
import time
import keyboard
import win32api
import win32con

#X:  726 Y:  397 RGB: (  0,   0,   0)
#X:  625 Y:  428 RGB: (181, 183, 231)
#X:  720 Y:  416 RGB: (180, 182, 231)
#X:  807 Y:  421 RGB: (178, 181, 230)
#These 4 comments above show the pixel value in x and y and their RGB value

time.sleep(5)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0, 0)
    

    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(726, 397)[0] == 0:
        click(726,397)
    if pyautogui.pixel(876, 397)[0] == 0:    
        click(876, 397)
    if pyautogui.pixel(1026, 397)[0] == 0:    
        click(1026, 397)
    if pyautogui.pixel(1176, 397)[0] == 0:    
        click(1176, 397)          