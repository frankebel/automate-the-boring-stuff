#!/usr/bin/env python
def displayInventory(inventory):
    assert isinstance(inventory, dict)

    total_items = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(v, k)
        total_items += v
    print(f'Total number of items: {total_items}')


def addToInventory(inventory, addedItems):
    assert isinstance(inventory, dict)
    assert isinstance(addedItems, list)
    
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)

