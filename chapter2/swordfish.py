#!/usr/bin/env python
while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue
    password = input('Hello, Joe. What is the password? (It is a fish.) ')
    if password == 'swordfish':
        break
print('Access granted.')

