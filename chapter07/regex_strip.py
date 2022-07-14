#!/usr/bin/env python
import re

def regex_strip(string, strip=None):
    """Implement strip() function with regex.

    If no strip character is passed, remove whitespace characters.
    """
    
    if strip is None:
        r = re.compile(r'\s')
    else:
        r = re.compile(strip)
    
    return r.sub('', string)


string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'

print(regex_strip(string))
print(regex_strip(string, 'Lorem'))

