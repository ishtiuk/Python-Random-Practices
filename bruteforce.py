import pyautogui
import string
import random

all_chars = string.ascii_letters + string.digits
print(type(all_chars))

usr_pass = pyautogui.password("Enter password: ")

while True:
    guess_pwd = random.choices(all_chars, k=len(usr_pass))
    print("<===========" + str(guess_pwd) + "===========>")
    if guess_pwd == list(usr_pass):
        hacked_pwd = ''.join(guess_pwd)
        print('hacked password: ', hacked_pwd)
        break