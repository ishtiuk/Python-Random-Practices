# from typing import Text


def check_prime(num):
    for i in range(2, num):
        print(i)
        if num % i == 0:
            return False
    return True
       

pri = check_prime(int(input()))

if pri is True:
    print('prime')
elif pri is False:
    print('not prime')