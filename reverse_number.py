inp = int(input("Enter a number: "))


xdl = 0

while inp > 0:
    lst_num = inp % 10
    xdl = xdl * 10 + lst_num
    inp //= 10

print('reversed number:',xdl)


print("\n::: But remember it's not applicable when the input number start with 0 like 0524, so here I have to reverse using string method\n")