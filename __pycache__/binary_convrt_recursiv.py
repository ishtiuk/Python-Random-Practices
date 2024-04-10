def binary_recursive(inpu):

    if inpu > 0:
        binary_recursive(inpu//2)
        print(inpu % 2, end='')                 # end='' is used to print all outputs together.


binary_recursive(int(input()))
