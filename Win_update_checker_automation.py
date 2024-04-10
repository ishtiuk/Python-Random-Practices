# import pyttsx3

# talke = pyttsx3.init()

# def talker(stt):
#     talke.say(stt)
#     talke.runAndWait()

# talker('&')


from time import sleep
import pyautogui

pyautogui.press('win')
pyautogui.sleep(1)
pyautogui.typewrite('settings')
pyautogui.sleep(5)
pyautogui.press('enter')
pyautogui.sleep(1.5)
pyautogui.typewrite('check for updates')
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.press('enter')


