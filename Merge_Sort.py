
def Merge_Sort(arr):
    if len(arr) > 1:
        q = len(arr) // 2
        L = arr[:q]
        M = arr[q:]

        Merge_Sort(L)
        Merge_Sort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = M[j]
                j += 1
            k += 1

        
        while i < len(L):
            arr[k] = L[i]
            i +=1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1
 


array = [45, 6, 4, 3, 24]

Merge_Sort(array)

print("Merge Sorted: ", array)

