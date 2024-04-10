
from types import AsyncGeneratorType


class Anything:
    no_of_pages = 787

    def __init__(self):
        self.nm = 'Smasher'

    def __repr__(self):
        return f"hey, I'm __repr__ 😎, but privilage is __str__ 🥴🥴"

    def __str__(self):
        return f"hey, I'm the privilage owner 😎😎😎"

obj = Anything()
print(obj)

# del Anything

print(Anything.no_of_pages)
