import datetime
from datetime import datetime
def get_days_from_today(date):
    try:
        time_now=datetime.today().date()
        fixed_date=datetime.strptime(date,"%Y-%m-%d")
        fixed_date=fixed_date.date()
        difference=time_now-fixed_date
        return difference.days
    except ValueError:
        return f"Please entern in format YYYY-MM-DD"
print(get_days_from_today("2022-02-24"))