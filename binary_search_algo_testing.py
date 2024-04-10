import time

# liner serch algorihm

lst = []

# for i in range(1, int(input("Enter: "))+1):
#     lst.append(i)                                     # used to print big list
# print(lst)


sort_list = [i for i in range(1000000)]

search = 8159
lower = 0
upper = len(sort_list)
inital = time.time()
while lower <= upper:
    mid = (lower + upper) // 2
    if sort_list[mid] == search:
        print(mid)
        break
    elif sort_list[mid] < search:
        lower = mid
    elif sort_list[mid] > search:
        upper = mid
    if search not in sort_list:
        print('errr')
        break
print((time.time()) - inital)