import csv
import time

inv = {}
items_quantity = []
table = []


# Counts how many items you have in total
def item_quantity(where):
    global items_quantity
    items_quantity = [where[values] for values in sorted(where, reverse=True)]
    return str(sum(items_quantity))


# List about your items
def item_table(inventory):
    global table
    table = [i for i in sorted(inventory, key=inventory.get, reverse=True)]
    return table


# Displays the inventory.
def display_inventory(inventory):
    global items_quantity, inv, table
    item_quantity(inv)
    item_table(inv)
    try:
        # If you type 'inventory' or 'inv', it's gonna show the whole inventory.
        if (inventory == "inventory") or (inventory == "inv"):
            print("\nInventory: ")
            for item in sorted(inv):
                print(str(item).capitalize()+": "+str(inv[item]))
            return "\nTotal number of items: "+str(sum(items_quantity))
        else:
            # If you want to check only one item.
            return "\n{} ".format(inv[inventory])+str(inventory).capitalize()+" you have."
    except KeyError:
        return "You don't have the {}...yet.".format(inventory.capitalize())


def add_to_inventory(inventory, added_items):
    global item_quantity, inv
    # Yeah, i was lazy wti that one
    inv = inventory
    loot_dict = {}
    n = 0
    for item in added_items:
        loot_dict.update({added_items[n]: added_items.count(added_items[n])})
        n += 1
    loot_list = [items for items in loot_dict]
    loot_list = sorted(loot_list)
    n = 0
    for i in loot_dict:
        if loot_list[n] in inv:
            inv.update({loot_list[n]: inv[loot_list[n]]+loot_dict[loot_list[n]]})
            n += 1
        else:
            inv.update({loot_list[n]: loot_dict[loot_list[n]]})
            n += 1
    item_quantity(inv)
    return "\nThe new item(s), Sir: "+str(loot_dict)+"\n"
    # Just in case...
    # for item in sorted(inv):
    #    print(str(item).capitalize()+": "+str(inv[item]))'
    # return "Total number of items: "+str(sum(items_quantity))+"\n---------------------------------------------"


def print_table(inventory=None, order=None):
    global inv, table
    item_table(inv)
    print("\nInventory:\ncount".rjust(5, ' '), "item name\n".rjust(20, ' '), "-".rjust(26, '-'))
    # Numeric order
    if order == "-count,desc":
        n = len(inv)
        for i in inv:
            print(str(inv[table[n-1]]).rjust(5, ' '), table[n-1].capitalize().rjust(20, ' '))
            n -= 1
    elif order == "count,desc":
        n = 0
        for i in inv:
            print(str(inv[table[n]]).rjust(5, ' '), table[n].capitalize().rjust(20, ' '))
            n += 1
    # Alphabetical order
    elif order == "count,asc":
        for item in sorted(inv):
            print(str(inv[item]).rjust(5, ' '), str(item).capitalize().rjust(20, ' '))
    elif order == "-count,asc":
        for item in sorted(inv, reverse=True):
            print(str(inv[item]).rjust(5, ' '), str(item).capitalize().rjust(20, ' '))
    # None? No problem!
    else:
        n = 0
        for i in inv:
            print(str(inv[table[n]]).rjust(5, ' '), table[n].capitalize().rjust(20, ' '))
            n += 1
        return "\nNo arguments senor?\n(e.g. inv, 'count,desc' or inv, 'count,asc')\nPsst, reverse goes with -"
    return "-".rjust(26, '-')


def import_inventory(inventory, filename="import_inventory.csv"):
    rfile = open(filename, "r")
    reader = csv.reader(rfile)
    basic_list = [i for i in reader]
    import_list = []
    n, m = 0, 0
    for i in basic_list:
        for i in basic_list[m]:
            import_list.append(basic_list[m][n])
            n += 1
        m += 1
        n = 0
    rfile.close()
    add_to_inventory(inventory, import_list)
    return rfile.close()


def export_inventory(inventory, filename):
    wfile = open(filename, "w")
    writer = csv.writer(wfile)
    slx = []
    slk = [i for i in inventory]
    slk = sorted(slk)
    n = 0
    for i in sorted(inventory):
        for i in range(inventory[i]):
            slx.append(slk[n])
        n += 1
    writer.writerow(slx)
    wfile.close()
    return "Done"
