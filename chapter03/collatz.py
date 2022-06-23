#!/usr/bin/env python
def collatz(number):
    match number % 2:
        case 0:
            number_new = number//2
        case 1:
            number_new = 3*number + 1
    print(number_new)
    return number_new


# Get user input
while True:
    try:
        num = int(input('Please enter a positive integer: '))
        break
    except ValueError:
        continue

# Execute until number is 1
while num > 1:
    num = collatz(num)

