import pyautogui
pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

for i in range(100):
    #pyautogui.write('Eu sou o mario\nA princesa esta em outro castelo\nIts me Mario ')
    #pyautogui.press('enter')
    pyautogui.press(['left','right'])

