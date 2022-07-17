#!/usr/bin/env python
import pyinputplus as pyip

# List and price all ingredients.
# bread
bread_types = ['wheat', 'white', 'sourdough']
bread_price = [1, 1, 1]
# protein
protein_types = ['chicken', 'turkey', 'ham', 'tofu']
protein_price = [0.8, 0.8, 0.8, 0.6, 1]
# cheese
cheese_types = ['cheddar', 'Swiss', 'mozzarella']
cheese_price = [0.5, 0.5, 0.5]
# extra
extra_list = ['mayo', 'mustard', 'lettuce', 'tomato']
extra_price = [0.2, 0.2, 0.3, 0.3]

price_total = 0

# Ask for sandwich composition.
# bread
bread = pyip.inputMenu(bread_types, numbered=True)
price_total += bread_price[bread_types.index(bread)]
# protein
protein = pyip.inputMenu(protein_types, numbered=True)
price_total += protein_price[protein_types.index(protein)]
# cheese
cheese_want = pyip.inputYesNo(prompt='Do you want cheese? ')
if cheese_want == 'yes':
    cheese = pyip.inputMenu(cheese_types, numbered=True)
    price_total += cheese_price[cheese_types.index(cheese)]
# extra
for i, item in enumerate(extra_list):
    item_want = pyip.inputYesNo(prompt=f'Do you want {item}? ')
    if item_want == 'yes':
        price_total += extra_price[i]
# Amount of sandwiches
amount = pyip.inputInt('How many sandwiches do you want? ', min=1)
price_total *= amount

# Return total price
print(f'Total price for sandwiches is: {price_total}')

