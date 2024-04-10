
array = [9, 7, 3, 1, 20, 12, 14]

for i in range(1, len(array)):
    item = array[i]
    j = i - 1

    while j >= 0 and item < array[j]:
        array[j + 1] = array[j]

        j -= 1

    array[j + 1] = item


print("Insertion Sort: ", array)