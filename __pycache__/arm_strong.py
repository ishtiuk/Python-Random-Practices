def check_armstrong(num):
    power = len(str(num))
    print(power, type(num))
    armstrong = 0
    temp_num = num

    while temp_num > 0:
        lst_digit = temp_num % 10
        armstrong += lst_digit ** power
        temp_num = temp_num // 10

    print(armstrong)
    print(num)
    print(temp_num)
    if armstrong == num:
        return 'number is armstrong'
    else:
        return "number isn't armstrong"


print(check_armstrong(int(input())))

        
