

def binary_serh_algo(sort, search):

    lower_bound = 0
    upper_bound = len(sort)
    print(upper_bound)

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        
        if sort[mid] == search:
            return mid

        elif sort[mid] < search:
            lower_bound = mid

        elif sort[mid] > search:
            upper_bound = mid 


lst = [2, 4, 7, 8, 9, 10, 65, 445]
#      0  1  2  3  4  5   6    7  
a = '4'
b = 'df'
sort = sorted(lst)
# lst.sort(reverse= False)
print(sort)               # The first Condition of Binary Search is list should be 'sorted' that means list should be 'Ascending Array or List'...!!!!!!!!
search = int(input('Enter: '))
print(binary_serh_algo(sort, search))