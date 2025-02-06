# Author: Rachel King
# Date: 02/06/2025
# Module 3 Lab - creating an interactive Coffee Shop simulator, including a receipt

# prints the shop name and asks the user for the number of products bought
print("***************************************")
print("Coffee Shop")
coffees = int(input("Number of coffees bought?\n"))
muffins = int(input("Number of muffins bought?\n"))
teas = int(input("Number of teas bought?\n"))
bagels = int(input("Number of bagels bought?\n"))
print("***************************************")

print() # blank line for spacing

# variable definitions for receipt
cost = (coffees * 5) + (muffins * 4) + (teas * 5) + (bagels * 3)
tax = cost * 0.06
total = cost + tax

# prints the receipt
print("***************************************")
print("Coffee Shop Receipt")
if coffees == 1:
    print(coffees, "Coffee at $5 each: $", coffees * 5)
if coffees > 1:
    print(coffees, "Coffees at $5 each: $", coffees * 5)
if muffins == 1:
    print(muffins, "Muffin at $4 each: $", muffins * 4)
if muffins > 1:
    print(muffins, "Muffins at $4 each: $", muffins * 4)
if teas == 1:
    print(teas, "Tea at $5 each: $", teas * 5)
if teas > 1:
    print(teas, "Teas at $5 each: $", teas * 5)
if bagels == 1:
    print(bagels, "Bagel at $3 each: $", bagels * 3)
if bagels > 1:
    print(bagels, "Bagels at $3 each: $", bagels * 3)
print("6% tax: $", round(tax, 3))
print("---------")
print("Total: $", total)
print("Thank you for your order!")
print("***************************************")
