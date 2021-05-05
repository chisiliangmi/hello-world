# for循环
def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + '  ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] += 1
            print("addedItems[{}]: {}".format(i, inventory[addedItems[i]]))
        else:
            inventory.setdefault(addedItems[i], 1)
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
