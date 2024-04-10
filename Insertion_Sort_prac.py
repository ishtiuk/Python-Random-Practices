
def Insertion_Sort(arr):

    for i in range(1, len(arr)):
        j = i - 1
        item = arr[i]

        
        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = item


    return arr




arr = [56, 3, 7, 4] + [i for i in range(50, -1, -1)]
print(Insertion_Sort(arr))
