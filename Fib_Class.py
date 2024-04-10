class Fib:
    def __init__(self, num):
        self.num = num
        self.i = 1
        self.a = self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.num:
            raise StopIteration

        if self.i <= 2:
            c = 1

        else:
            c = self.a + self.b
            self.b = self.a
            self.a = c

        self.i += 1
        return c



for i in Fib(5):
    print(i)