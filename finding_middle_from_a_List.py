
lst = [1, 2, 3, 2, 5, 6, 7, 14]

if len(lst) % 2 != 0:
    indx = len(lst) // 2
    middle = lst[indx]

elif len(lst) % 2 == 0:
    indx1 = len(lst) // 2
    indx2 = (len(lst) // 2) - 1
    # indx2 = indx1 - 1         <<--- this can be applicable too..

    middle = (lst[indx1] + lst[indx2]) // 2

print(middle)