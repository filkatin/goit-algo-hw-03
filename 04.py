
from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users):
    today = datetime.strptime("2024.01.22"[5:], "%m.%d")
    users_birthdays = []
    i = 0
    while i < len(users):
        diff = datetime.strptime(users[i]["birthday"][5:], "%m.%d") - today
        if diff < timedelta(days=7) and diff >= timedelta(days=0):
            users_birthdays.append(users[i])
        i += 1    
    
    return users_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)