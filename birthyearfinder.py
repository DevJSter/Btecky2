birth_year=int(input("Enter your Birth Year"))
age=2023-birth_year
print("Your age is ",age)







from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day):
    current_date = datetime.now()
    birth_date = datetime(birth_year, birth_month, birth_day)
    age = current_date.year - birth_date.year

    # Check if the birthday has already occurred this year
    if (
        current_date.month < birth_date.month
        or (current_date.month == birth_date.month and current_date.day < birth_date.day)
    ):
        age -= 1

    return age

# Example usage
birth_year = int(input("Enter the birth year: "))
birth_month = int(input("Enter the birth month: "))
birth_day = int(input("Enter the birth day: "))

age = calculate_age(birth_year, birth_month, birth_day)
print("The person is", age, "years old.")









from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age(birth_year, birth_month, birth_day):
    current_date = datetime.now()
    birth_date = datetime(birth_year, birth_month, birth_day)
    age_delta = relativedelta(current_date, birth_date)

    years = age_delta.years
    months = age_delta.months
    weeks = age_delta.weeks
    days = age_delta.days

    return years, months, weeks, days

# Example usage
birth_year = int(input("Enter the birth year: "))
birth_month = int(input("Enter the birth month: "))
birth_day = int(input("Enter the birth day: "))

years, months, weeks, days = calculate_age(birth_year, birth_month, birth_day)
print(f"The person is {years} years, {months} months, {weeks} weeks, and {days} days old.")
