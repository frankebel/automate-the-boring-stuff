#!/usr/bin/env python
import pyinputplus as pyip

# List and price all ingredients.
bread = {'wheat': 1, 'white': 1, 'sourdough': 1}
protein = {'chicken': 0.8, 'turkey': 0.8, 'ham': 0.6, 'tofu': 1}
cheese = {'cheddar': 0.5, 'Swiss': 0.5, 'mozzarella': 0.5}
extra = {'mayo': 0.2, 'mustard': 0.2, 'lettuce': 0.3, 'tomato': 0.3}

price_total = 0

# Ask for sandwich composition.
# bread
bread_type = pyip.inputMenu(list(bread.keys()), numbered=True)
price_total += bread[bread_type]
# protein
protein_type = pyip.inputMenu(list(protein.keys()), numbered=True)
price_total += protein[protein_type]
# cheese
cheese_want = pyip.inputYesNo(prompt='Do you want cheese? ')
if cheese_want == 'yes':
    cheese_type = pyip.inputMenu(list(cheese.keys()), numbered=True)
    price_total += cheese[cheese_type]
# extra
for item, price in extra.items():
    item_want = pyip.inputYesNo(prompt=f'Do you want {item}? ')
    if item_want == 'yes':
        price_total += price
# Amount of sandwiches
amount = pyip.inputInt('How many sandwiches do you want? ', min=1)
price_total *= amount

# Return total price
print(f'Total price for sandwiches is: {price_total}')

