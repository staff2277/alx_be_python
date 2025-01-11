from datetime import datetime, date, timedelta

def calculate_future_date(current_date, days_to_add):
    return current_date + timedelta(days=days_to_add)

def display_current_datetime():
    current_datetime = datetime.now()
    print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

    current_date = date.today()

    days_to_add = int(input("Enter the number of days to add to the current date: "))

    future_date = calculate_future_date(current_date, days_to_add)

    print("Future date:", future_date.strftime("%Y-%m-%d"))

display_current_datetime()
