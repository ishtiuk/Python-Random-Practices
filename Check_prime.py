#

def prime_checker(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num_passing = prime_checker(int(input()))

if num_passing:
    print('PRIME')

else:
    print('NOT PRIME')