#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        if arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, qty_str = arg.split(":")
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            quantity = int(qty_str)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue
        inventory[item] = quantity
    total = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} "
          f"items: {total}")
    if total != 0:
        for item in inventory:
            percent = round(inventory[item] * 100 / total, 1)
            print(f"Item {item} represents {percent}%")
    most_item: str | None = None
    least_item: str | None = None
    for item in inventory:
        if most_item is None or inventory[item] > inventory[most_item]:
            most_item = item
        if least_item is None or inventory[item] < inventory[least_item]:
            least_item = item
    if most_item is not None and least_item is not None:
        print(f"Item most abundant: {most_item} "
              f"with quantity {inventory[most_item]}")
        print(f"Item least abundant: {least_item} "
              f"with quantity {inventory[least_item]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
