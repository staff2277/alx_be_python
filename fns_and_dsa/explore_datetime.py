import datetime



def display_current_datetime ():
    current_date = datetime.datetime.now()
    
    print(current_date.strftime("%Y-%m-%d"))

    current_date = datetime.date.today()

    days_to_add = int(input("Enter a number: "))

    future_date = current_date + datetime.timedelta(days=days_to_add)

    print(future_date.strftime("%Y-%m-%d"))


display_current_datetime()
