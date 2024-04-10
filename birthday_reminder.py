from datetime import datetime


def birthday_processor(birthday):
    try:
        processed_birthday = datetime.strptime(birthday, "%d/%m/%Y")
        
    # except TypeError as tyep:
    #     print("Error:: ", tyep)
    #     # return processed_birthday
    # except ValueError as tp:
    #     print("Err:: ", tp)
    #     # return processed_birthday
    except:
        pass
        # print(tr)
    return processed_birthday

def next_birthday(now_birthday):
    now = datetime.now()
    this_year_birthday = datetime(now.year, now_birthday.month, now_birthday.day)
    print(this_year_birthday)

    birthday = (this_year_birthday - now).days

    if birthday < 0:
        nxt_year = datetime(now.year+1, now_birthday.month, now_birthday.day)
        birthday = (nxt_year - now).days
    return birthday

    
yt = input("DD/MM/YYYY:: ")
prin = birthday_processor(yt)
birthday_comming = next_birthday(prin)
print("Your birthday coming in:", birthday_comming, "days")