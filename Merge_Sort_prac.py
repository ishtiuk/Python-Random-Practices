
def Merge_Sort(arr):
    if len(arr) > 1:
        q = len(arr) // 2
        L = arr[:q]
        M = arr[q:]
        
        Merge_Sort(L)
        Merge_Sort(M)

    # print(arr)          ## NOTE: for survellence

        i = j = k = 0      ## "i" L pointer, "j" M pointer, "k" arr pointer
        print(arr)

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
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1



arr = [45, 6, 335, 655, 44, 289]
print(Merge_Sort(arr))