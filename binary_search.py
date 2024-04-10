lst = [5,  6, 67, 76, 88, 477, 977, 1000]

lower_range = 0
upper_range = len(lst)

search = 88

while lower_range <= upper_range:
    mid = (lower_range + upper_range) // 2

    if lst[mid] == search:
        print(lst[mid], mid)
        break

    elif lst[mid] > search:
        upper_range = mid

    elif lst[mid] < search:
        lower_range = mid

    if search not in lst:
        print('sorry element does not exist')
        break