"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
import time

class InvalidDate(Exception):
    pass


def calculate_days(input_date):
    try:
        dt = datetime.strptime(input_date, "%Y-%m-%d")
        input = dt.date()
    except:
        raise InvalidDate("WrongFormatException")   
    
    today_date=datetime.now().date()
    if input>today_date:
        diff=input-today_date
    else:
        diff=today_date-input
    return diff
input_date=input("Enter the date")
difference=calculate_days(input_date)
print(difference)  