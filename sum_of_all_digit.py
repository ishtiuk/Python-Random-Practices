# import datetime

# birth = input('DD/MM/YYYY: ')

# birthday = datetime.datetime.now()
# # print(birthday)
# bt = datetime.datetime.strptime(birth, '%d/%m/%Y')
# print(bt)
# print(type(bt))


# this_year_birthday = datetime.datetime(birthday.year, bt.month, bt.day)
# print(this_year_birthday)


indf = int(input())
sumd = 0
while indf > 0:
    lst_dighit = indf % 10
    sumd += lst_dighit
    indf = indf // 10
print(sumd)

