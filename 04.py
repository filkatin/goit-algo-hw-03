
from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users):
    today = datetime.strptime("2024.01.22", "%Y.%m.%d")
    users_greeting_dates = []

    i = 0
    while i < len(users):
        diff = datetime.strptime(users[i]["birthday"][5:], "%m.%d") - datetime(1900, today.month, today.day)
        print(diff)
        if diff >= timedelta(days=0):
            users[i]["birthday"] = str(today.year) + users[i]["birthday"][4:10]
            user_bday = datetime.strptime(users[i]["birthday"], "%Y.%m.%d")
            if user_bday.isoweekday() in set((6, 7)):
                users[i]["birthday"] = (user_bday + timedelta(days=8 - user_bday.isoweekday())).strftime("%Y.%m.%d")
        else:  
            users[i]["birthday"] = str(today.year+1) + users[i]["birthday"][4:10]
            user_bday = datetime.strptime(users[i]["birthday"], "%Y.%m.%d")
            if user_bday.isoweekday() in set((6, 7)):
                users[i]["birthday"] = (user_bday + timedelta(days=8 - user_bday.isoweekday())).strftime("%Y.%m.%d")
            
        print(users[i]["birthday"])
        users_greeting_dates.append(users[i])
        i += 1

    return users_greeting_dates


users = [
    {"name": "workday", "birthday": "2024.01.05"},
    {"name": "saturday", "birthday": "2024.01.06"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)