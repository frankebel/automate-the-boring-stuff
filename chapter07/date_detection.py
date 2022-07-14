#!/usr/bin/env python
import datetime
import re

def detect_date(string):
    """Regex to find valid date in string.

    Format is DD/MM/YYYY.
    Year must be in [1000, 2999].
    """

    date_regex = re.compile(r'^([0-2][0-9]|3[01])\/(0[1-9]|1[0-2])\/([12]\d{3})$')
    return re.search(date_regex, string).groups()

def valid_date(day, month, year):
    """Check if the input date (strings) is a valid date."""

    try:
        datetime.date(year=int(year), month=int(month), day=int(day))
        return True
    except ValueError:
        return False


date = '31/09/1999'

try:
    day, month, year = detect_date(date)
except AttributeError:
    print('Could not detect date.')
    exit() 

if valid_date(day, month, year):
    print(datetime.date(year=int(year), month=int(month), day=int(day)).isoformat())
else:
    print('Found a non-valid date.')

