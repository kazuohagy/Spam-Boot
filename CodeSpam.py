import pyautogui, time
time.sleep(4)
m = open("Shrek.txt","r")
pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

for each_line in m:
    pyautogui.typewrite(each_line)
    pyautogui.press('enter')

#for i in range(100):
    #pyautogui.write('Eu sou o mario\nA princesa esta em outro castelo\nIts me Mario ')
    #pyautogui.press('enter')
 #   pyautogui.press(['left','right'])

