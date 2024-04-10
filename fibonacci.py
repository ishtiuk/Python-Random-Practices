
def fibo(n):
    a = 1
    b = 1
    c = 0

    if n > 0 and n <= 2:
        return 1

    for i in range(3, n+1):  
        c = a + b
        b = a
        a = c

    return c




n = int(input("Enter number to get fibonacci: "))
print(fibo(n))

# get all fibs till the number...

def fibo(n):
    a = 1
    b = 1
    c = 0


    for i in range(1, n+1):  

        if i > 0 and i <= 2:
            yield i

        else:    
            c = a + b
            b = a
            a = c

            yield c


fibs = list(fibo(10))
print(fibs)