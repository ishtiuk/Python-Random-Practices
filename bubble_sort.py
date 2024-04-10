lst = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]


for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp
    print(lst)



# Bubble Sorting Algorithm Continuosly Compares two pashapashi Elements and swaps them

# finally gives us a Sorted List.....






a = 5
b = 7

temp = a

a = b
b = temp
print(a, b)