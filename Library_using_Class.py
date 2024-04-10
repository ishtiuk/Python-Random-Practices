
class Library:
    management_corpo = 'The HxD Corpo'

    def __init__(self, lib_nm, books):
        self.lib_name = lib_nm
        self.books = books
        self.users = {}
        self.lended_books = []
        self.donators = {}
        

    def lend_books(self, user_nm, book_nm):
        if book_nm in self.books:
            self.users[book_nm] = user_nm
            indx = self.books.index(book_nm)
            lent = self.books.pop(indx)
            self.lended_books.append(lent)
            print('Process Successful')
            print(book_nm, 'was indexed at user:', user_nm)
        elif book_nm not in self.books:
            print('Sorry, Sir. This book is Currently Unavailbe now')
            try:
                print(book_nm, 'belongs to user:', self.users[book_nm])
            except:
                pass

    def add_book(self, donator, book_nm):
        self.books.append(book_nm)
        self.donators[book_nm] = donator

    def all_books(self):
        print('                 <<== Our BOOks ==>>')
        for i in self.books:
            print(i, end=' || ')

    def see_donators_according_bk_nm(self, book_nm):
        if book_nm in self.donators:
            print('This book is donated by:', self.donators[book_nm])
        else:
            print('This book is exist by Default in Our Library')

    def thanking(self):
        return f"Thanks for Staying with {self.lib_name}. Powered by {self.management_corpo}"

        # try:                                                                        # <--- this technique also Applicable 😎😎
        #     print('This book is donated by:', self.donators[book_nm])
        # except:
        #     print('This book is exist by Default in Our Library')

lst_books = ['ANNA', 'INVISIBLE', 'KARENINA','QUIXOTE', 'GRETA', 'GARBO', 'KARENINA','MOCKINGBIRD',
'KILL', 'MOCKINGBIRD', 'THE', 'GREAT', 'GATSBY',  'HUNDRED', 'YEARS', 'SOLITUDE',
'PASSAGE', 'INDIA', 'BELOVED']


rohim_lib = Library('Rohim Library', lst_books)

def usr_interface():
    inpu = input('''Enter 'A' to see all Books
    Enter 'L' to lend Books
    Enter 'D' to Donate Books
    Enter 'ER' to see Donators
    Enter 'S' to see Donator according to Book name
    Enter 'E' to exit anytime
    :: ''').upper()
    
    if inpu == 'E':
        print('Exiting')
        print(rohim_lib.thanking())
        exit()

    if inpu == 'A':
        rohim_lib.all_books()

    elif inpu == 'L':
        rohim_lib.lend_books(input('username: ').lower(), input('book name: ').upper())

    elif inpu == 'D':
        rohim_lib.add_book(input('username or name: ').lower(), input('book name: ').upper())

    elif inpu == 'ER':
        print(rohim_lib.donators)

    elif inpu == 'S':
        rohim_lib.see_donators_according_bk_nm(input('Book name: ').upper())

    else:
        print('Invalid input')

while True:
    usr_interface()


