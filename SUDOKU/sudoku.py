import numpy as np

arr = np.array(np.zeros((9, 9)), np.int8)


def board_printer(arr):
    print("+---" * arr.shape[1] , "+", sep='')

    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            print("|", arr[r, c], "", end='')
        print("|")
        print("+---" * arr.shape[1] , "+", sep='')
    

board_printer(arr)