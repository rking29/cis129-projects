# Author: Rachel King
# Date: 02/04/2025
# Module 3 Lab - creating an interactive Coffee Shop simulator, including a receipt

# prints the shop name and asks the user for the number of coffees and muffins bought
print("***************************************")
print("My Coffee and Muffin Shop")
coffees = int(input("Number of coffees bought?\n"))
muffins = int(input("Number of muffins bought?\n"))
print("***************************************")

print() # blank line for spacing

# variable definitions for receipt
cost = (coffees * 5) + (muffins * 4)
tax = cost * 0.06
total = cost + tax

# prints the receipt
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
if coffees == 1:
    print(coffees, "Coffee at $5 each: $", coffees * 5)
if coffees > 1:
    print(coffees, "Coffees at $5 each: $", coffees * 5)
if muffins == 1:
    print(muffins, "Muffin at $4 each: $", muffins * 4)
if muffins > 1:
    print(muffins, "Muffins at $4 each: $", muffins * 4)
print("6% tax: $", tax)
print("---------")
print("Total: $", total)
print("***************************************")
