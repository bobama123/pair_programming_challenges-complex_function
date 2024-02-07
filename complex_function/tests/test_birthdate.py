import pytest
from lib.birthdate import *

def test_for_access_denied_date_2022():
    result = age_checker("2022-12-12")
    assert result == "Your access is denied, your current age is 1 and required age is 16."


def test_for_access_granted_date_2003():
    result = age_checker("2003-12-12")
    assert result == "Your access is granted."


def test_for_raise_error_for_format():
    with pytest.raises(Exception) as e:
        age_checker("2003.12.12")
    error = str(e.value)
    assert error == "Invalid date format"

def test_for_access_granted_date_today_2008():
    result = age_checker("2008-02-07")
    assert result == "Your access is granted."

def test_for_access_granted_date_today():
    result = age_checker("2024-02-07")
    assert result == "Your access is denied, your current age is 0 and required age is 16."