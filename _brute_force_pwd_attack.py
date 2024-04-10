import pyautogui
import string
import random

alpha = string.ascii_letters
digits = string.digits

all_chars = alpha + digits

user = pyautogui.password('Enter: ')

lst_usr = list(user)

while True:
    rand_choise = random.choices(all_chars, k=len(lst_usr))
    print("<===========" + str(rand_choise) + "===========>")
    if rand_choise == lst_usr:
        hkd_pwd = ''.join(rand_choise)
        print('pwd: ', hkd_pwd)
        break 