array = [5, 4, 2, 10]
length = len(array)
array = array + [0]


index = 0
value = 12

for i in range(length, -1, -1):
    if i == index:
        array[index] = value
        break

    array[i] = array[i - 1]



print(array)
