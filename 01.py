from datetime import datetime
from datetime import date as date1

def get_days_from_today(date):
    date_format = '%Y-%m-%d'
    try:
        date_formated = datetime.strptime(date, date_format).date()
        now = date1.today()
        diff = str(now-date_formated).split(',')[0]
        return diff
    except ValueError:
        print("Input string is not date in format 'РРРР-ММ-ДД' ")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")  


print("Result: ", get_days_from_today("2021-10-09"))