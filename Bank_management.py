
class Bank:
    Bank_nm = '【Ｃｙｂｅｒ　Ｐａｒａｄｉｓｅ　Ｓｏｆｔｗａｒｅ　Ｄｅｖ　Ｕｎｉ】'

    def __init__(self, ac_holder, balance):
        self.ac_holder = ac_holder
        self.__bal = balance


    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.__bal:
            self.__bal -= withdraw_amount
            print('Withdrwal Succeed')
            print("Here's your Withdrawal:",withdraw_amount,'Cash')
        else:
            print("Sorry, Sir. You haven't sufficient Balance for Withdrawal")

    def deposit(self, depo_amount):
        self.__bal += depo_amount
        print('Deposit Succeed')

    def check_balance(self):
        return f"{self.ac_holder}'s Current Balance: {self.__bal}"

    @staticmethod
    def thanking():
        print('''Thanks for Staying with Us, Sir
        Have a Nice Day''')
    
    def software_dev_corpo(self):
        print('||  Powered by', self.Bank_nm,'||')
        

Our_Bank = Bank(input('Enter Ac_holder: ').lower(), float(input('Enter Balance: ')))


def usr_interface():
    usr = input('''
    Enter 'C' to Check Balance
    Enter 'W' to Withdraw
    Enter 'D' to Deposit
    Enter 'E' to exit
    :: ''').upper()

    if usr == 'E':
        Our_Bank.thanking()
        Our_Bank.software_dev_corpo()
        exit()

    if usr == 'C':
        print(Our_Bank.check_balance())

    elif usr == 'W':
        Our_Bank.withdraw(float(input('Enter Amount: ')))

    elif usr == 'D':
        Our_Bank.deposit(float(input('Enter Amount: ')))

    else:
        print('Sorry. Invalid Input')


while True:
    usr_interface()

