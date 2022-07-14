#!/usr/bin/env python
import re

def is_strong(password):
    """Check if a password is strong and return boolean.

    A strong password has at least 8 characters,
    contains both uppercase and lowercase letters,
    and has at least one digit.
    """

    # Check for at least 8 characters.
    length = re.compile(r'\w{8,}')
    if length.search(password) is None:
        return False

    # Contain uppercase, lowercase, digit.
    characters = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)')
    if characters.search(password) is None:
        return False

    return True

password = 'aRstnei0'
print(is_strong(password))

