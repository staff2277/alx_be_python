from datetime import datetime, date, timedelta

def calculate_future_date(current_date, days_to_add):
    # Calculate the future date by adding the specified number of days
    return current_date + timedelta(days=days_to_add)

def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()
    print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

    # Get the current date
    current_date = date.today()

    # Ask the user to input a number of days to add
    days_to_add = int(input("Enter a number of days to add: "))

    # Calculate the future date using the calculate_future_date function
    future_date = calculate_future_date(current_date, days_to_add)

    # Print the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Call the function to display current and future date
display_current_datetime()
