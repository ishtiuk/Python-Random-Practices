

def string_palin_chk_unit():
    sentence = input("Enter a sentence: ")
    if sentence == sentence[::-1]:
        print(sentence,':: palindrome')
    else:
        print(sentence,':: not palindrome')

def num_palin_chk_unit():
    num = int(input("Enter a number: "))
    temp = num
    reverse_num = 0
    while temp > 0:
        lst_num = temp % 10
        reverse_num = reverse_num * 10 + lst_num
        temp //= 10

    if reverse_num == num:
        print(num, 'is palindrome')
    else:
        print(num, 'is not palindrome')
    

usr_choice = int(input("|| Do you want to check a num or string if it palindrome? ||\n Enter 1 to check string\n Enter 2 to check num: "))

if usr_choice == 1:
    string_palin_chk_unit()
elif usr_choice == 2:
    num_palin_chk_unit()
else:
    print('sorry invalid selection')