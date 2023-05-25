import pyautogui
import pyautogui as op


op = pyautogui.confirm('choose: ', buttons = ['libreoffice'])

if op == 'libreoffice':
    pyautogui.hotkey('Ctrl', 'Alt', 't')
    pyautogui.sleep(4)
    pyautogui.write('touch file.odt Desktop')
    pyautogui.sleep(4)
    pyautogui.press('enter')
    pyautogui.sleep(4)
    pyautogui.write('libreoffice file.odt')
    pyautogui.press('enter')