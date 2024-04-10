
def Shell_Sort(arr):
    size = len(arr)
    gap = size // 2
    i = 0                   ## NOTE: "i" just for counting number of iterations 😁, serveillence

    while gap > 0:

        for i in range(gap, size):
            item = arr[i]
            j = i

            while j >= gap and item < arr[j - gap]:
                arr[j] = arr[j - gap]
                i += 1                  ## NOTE: "i" just for counting number of iterations 😁, serveillence                  
                j -= gap


            arr[j] = item

        gap = gap // 2
    

    print(arr, i)


array = [42, 21, 22, 5, 3, 7, 0, 12, 28, 14, 35, 49, 56, 70, 63, 88]
Shell_Sort(array)
