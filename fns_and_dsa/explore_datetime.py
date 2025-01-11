from datetime import datetime, date, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    print("Current date and time:", current_datetime.strftime("%Y-%m-%d"))

    current_date = date.today()

    days_to_add = int(input("Enter a number of days to add: "))

    future_date = current_date + timedelta(days=days_to_add)

    print("Future date:", future_date.strftime("%Y-%m-%d"))

display_current_datetime()
