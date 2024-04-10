
def print_Exception_Tree(cls, loop=0):
    

    if loop < 1:
        print("+---", end='')
    if loop > 1:
        print(" |" * loop, end=" ")

    print(cls.__name__)

    for el in cls.__subclasses__():
        loop += 1
        print_Exception_Tree(el, loop)


print_Exception_Tree(BaseException)