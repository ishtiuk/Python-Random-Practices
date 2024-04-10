import datetime

hour = datetime.datetime.now().hour                          # to print the current hour, here hour is 'int' type, it will become str if we write hour = str(hour)
print("current hour:",hour)

minute = datetime.datetime.now().minute                     # to print the current minute, here minute is also 'int' type,
print("current minute:",minute)

second = datetime.datetime.now().second                     # to print the current second, here second is also 'int' type,
print("current second:",second)


now_time_international = datetime.datetime.now().strftime("%H:%M")        # here datetime.datetime.now().strftime('%H %M) , %H used to print hour in international format 
print("current time with hour & minute in international format:",now_time_international) # and %M used to print minute

now_time_local = datetime.datetime.now().strftime("%I %M %S")          # here datetime.datetime.now().strftime("%I %M %S") , %I used to print hour in local format
print("current time with hour, minute, second in local format:", now_time_local) # and %M used to print minute, %S used to print second

now_time_local_PM_AM = datetime.datetime.now().strftime("%I %M %S %p") # here datetime.datetime.now().strftime("%I %M %S %p"), %I used to hour local, %M to minute, %S to second
print("current time with hour, minute, second in local format with AM or PM:",now_time_local_PM_AM)                                            # %p used to print AM or PM




now_full_date = datetime.datetime.now().strftime("%D")            # here datetime.datetime.now().strftime("%D"), %D is used to print current date fully, including date, month and year
print("current full date including date, month & year: ",now_full_date)

now_month = datetime.datetime.now().strftime("%h")        # here datetime.datetime.now().strftime("%h"), %h is used to print current month name
print("current month name:",now_month)

now_month_number = datetime.datetime.now().strftime("%m")  # here datetime.datetime.now().strftime("%m"), %m is used to print current month number
print("current month number:",now_month_number) 

now_year = datetime.datetime.now().strftime('%y')     # here datetime.datetime.now().strftime('%y'), %y is used to print current year number
print("current year:", now_year)



# print('''<<<================== important notice ==================>>>
# lowercase ==== lowercase %y = year number, %m = month number, %h = month name, %p = for AM or PM
# \nuppercase ==== uppercase %H = hour in international, %I hour in local, %M = minute, %S = second''')


                    #    _____________________________________

data = input("DD/MM/YYYY: ")
today = datetime.datetime.strptime(data, '%d/%m/%Y')
print(today)