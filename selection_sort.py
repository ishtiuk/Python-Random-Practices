lst = [55, 44, 33, 32, 75, 23, 64, 12, 99]





for i in range(len(lst)):

    min_indx = i

    for j in range(i, len(lst)):
        
        if lst[min_indx] > lst[j]:
            min_indx = j
    print(lst)
    temp = lst[i]
    lst[i] = lst[min_indx]
    lst[min_indx] = temp
    # print(lst)


print('\n',lst)