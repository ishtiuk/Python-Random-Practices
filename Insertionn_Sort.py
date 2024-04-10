
arr = [5, 4, 2, 1]
length = len(arr)


for i in range(1, length):
    item = arr[i]
    j = i - 1

    while j >= 0 and item < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = item


print("Insertion Sorted: ", arr)