#!/usr/bin/env python
def comma_code(param):
    assert isinstance(param, list)

    result = ''
    for i, element in enumerate(param):
        if i != 0:
            # Not first element in list.
            result = result + ', '
        if i == len(param)-1:
            # Last element in list.
            result = result + 'and '
        result = result + element
    return result


spam = ['apples' , 'bananas', 'tofu', 'cats']
print(comma_code(spam))
print(comma_code([]))

