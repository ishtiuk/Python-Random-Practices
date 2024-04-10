
arr = [5, 3, 9, 3, 56, 34, 29, 1]

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("bubble sorted: ", arr)




arr2 = [5, 3, 7, 2, 1, 6, 4]

for i in range(len(arr2)):
    mini = i

    for j in range(i+1, len(arr2)):
        if arr2[j] < arr2[mini]:
            mini = j
    # print(mini, arr2[mini])

    temp = arr2[i]
    arr2[i] = arr2[mini]
    arr2[mini] = temp

print("selection sorted: ", arr2)

