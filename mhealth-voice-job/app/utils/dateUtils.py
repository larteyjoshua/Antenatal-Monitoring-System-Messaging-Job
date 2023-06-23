from datetime import date, timedelta


def count_days(start_date):
    passDate = date.fromisoformat(start_date)
    today = date.today()
    one_day_from_today = today + timedelta(days=1)
    return passDate == one_day_from_today
