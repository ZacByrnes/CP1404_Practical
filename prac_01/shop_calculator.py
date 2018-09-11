
"""
num_items = int(input('Enter the amount of items purchased.'))
while num_items > 0:
    if num_items > 0:
        item_price = float(input('Enter the price of the item: $'))
    num_items = num_items - 1
    total_price += item_price

print('Number of items: ', abs(num_items))

print('Total price for ', abs(num_items), ' items is $', total_price)
"""
MENU = """A - Add another item
F - Finish shopping
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
num_items = 0
total_price = 0
while choice != "Q":
    if choice == "A":
        item_price = float(input('Enter the price of the item: $'))
        print('Price of item: $', item_price)
        total_price = total_price + item_price
        num_items = num_items + 1
    elif choice == "F" and num_items > 0:
        if total_price > 100:
            total_price_adj = total_price - total_price * 0.1
            print('There are', num_items, 'items and the total price for', num_items, 'items is $', "%.2f" % round(total_price_adj, 2))
        else:
            print('There are', num_items, 'items and the total price for', num_items, 'items is $', "%.2f" % round(total_price, 2))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you for shopping with us!")