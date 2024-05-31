"""
get number of items
total_price = 0

for number in range(number of items)
    get item_price
    total price = total price + item_price

if total price > 100
    discount = total price * 0.10
else
    discount = 0

final price = total price - discount
print final price
"""

number_items = int(input("Number of items: "))
total_price = 0

for number in range(number_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    discount = total_price * 0.10
else:
    discount = 0

final_price = total_price - discount
print(f"{final_price:.2f}")

