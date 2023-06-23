from datetime import date, timedelta


def count_days(start_date):
    passDate = date.fromisoformat(start_date)
    today = date.today()
    return passDate == today
