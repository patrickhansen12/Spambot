import pyautogui,time
import keyboard # using module keyboard
time.sleep(5)

f= open("beemovie.txt","r")
for word in f:
    if(keyboard.is_pressed("f6")):
        break

    pyautogui.typewrite(word)
    pyautogui.press("enter")
   
