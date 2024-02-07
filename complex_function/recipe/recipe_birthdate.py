## 1. Describe the Problem

# As an admin
# So that I can determine whether a user is old enough
# I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

# As an admin
# So that under-age users can be denied entry
# I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

# As an admin
# So that old enough users can be granted access
# I want to send a message to any user aged 16 or older to say that access has been granted.

# As an admin
# So that invalid entries are rejected
# I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

# _Include the name of the function, its parameters, return value, and side effects._

def age_checker(birth_date):
    #Parameters: a string for date of birth (YYYY-MM-DD)
    #Returns string if access denied or granted. (If denied, string of current age and required age)
    #Raises error if parameter in wrong format





## 3. Create Examples as Tests

#_Make a list of examples of what the function will take and return._


# EXAMPLE

"""
Given date of birth is 2022-12-12
Returns access denied, with current age and required age
"""

age_checker("2022-12-12") > "Your access is denied, your current age is {1} and required age is 16"

"""
Given date of birth is 2003-12-12
Returns access granted.
"""

age_checker("2003-12-12") > "Your access is granted"

"""
Given date of birth is 2003.12.12
Raises error
"""

age_checker("2003.12.12") > "Invalid date format"

"""
Given date of birth is 2024-02-07
Returns access denied, with current age and required age
"""

age_checker("2008-02-07") > "Your access is granted"



## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
