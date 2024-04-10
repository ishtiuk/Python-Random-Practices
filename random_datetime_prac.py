from datetime import datetime

birthday = input("Enter your birthday DD/MM/YYY: ")

# try:
    
    
# except:
#     pass
format_birthday = datetime.strptime(birthday, "%d/%m/%Y")
print("type of", type(format_birthday))
print(format_birthday)

