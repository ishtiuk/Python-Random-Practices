import os
import pyautogui

argu = input('''
Enter 1 to open CMD
Enter 2 to open Powershell :: ''')

if argu == '1':
    try:
        os.startfile('%windir%\\system32\\cmd.exe')
    except FileNotFoundError as fileerr:
        print(fileerr)
        os.startfile('C:\\Windows\\System32\\cmd.exe')
        pyautogui.sleep(3)
        pyautogui.typewrite('python')
        pyautogui.press('enter')
        # os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

elif argu == '2':
    try:
        os.startfile('%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe')
    except FileNotFoundError as erjk:
        print(erjk) 
        os.startfile('"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"')


