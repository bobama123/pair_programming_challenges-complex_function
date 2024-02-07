import re
from datetime import datetime

def age_checker(birth_date):
    if bool(re.match(r"^\d{4}-\d{2}-\d{2}$", birth_date)) == False:
        raise Exception("Invalid date format")

    age = ((datetime.now() - datetime.strptime(birth_date, "%Y-%m-%d"))/365).days
    if age < 16:
        return f"Your access is denied, your current age is {age} and required age is 16."
    else:
        return "Your access is granted."