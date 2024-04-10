usr_num = int(input("Enter number a check armstrong: "))
lenght = len(str(usr_num))
temp = usr_num

armstrong = 0

while temp > 0:
    lst_num = temp % 10
    armstrong = armstrong + lst_num ** lenght
    temp = temp // 10

if usr_num == armstrong:
    print(usr_num, 'is an armstrong')
else:
    print(usr_num, "isn't an armstrong")