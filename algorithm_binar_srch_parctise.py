# binary Search Algorithm

lst = [5, 6, 7, 57, 75, 78, 100]

lwr_range = 0
upr_range = len(lst)

search = 100

while lwr_range <= upr_range:
    mid = (lwr_range + upr_range) // 2
    
    if lst[mid] == search:
        print(f"{search} index no: {mid}")
        break

    elif lst[mid] < search:
        lwr_range = mid

    elif lst[mid] > search:
        upr_range = mid

    
# Bubble Sorting Algorithm

arr1 = [6, 4, 3, 2, 454, 646]


for i in range(len(arr1)):
    for j in range(len(arr1) - 1):
        if arr1[j] > arr1[j + 1]:
            temp = arr1[j]
            arr1[j] = arr1[j + 1]
            arr1[j + 1] = temp


print(arr1)



# Selection Sorting Algorihm 

arr2 = [9, 7, 6, 4, 3, 2]


for i in range(len(arr2)):

    mini = i

    for j in range(i+1, len(arr2)):
        if arr2[mini] > arr2[j]:
            mini = j

    temp = arr2[mini]
    arr2[mini] = arr2[i]
    arr2[i] = temp

print(arr2)