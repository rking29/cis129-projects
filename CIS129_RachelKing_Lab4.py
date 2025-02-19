# Module 5 Lab-4
# Rachel King
# 02/19/25
# calculates bonus amounts for a store and its employees based on their sales

# the main function
def main():
    monthlySales = getSales("Enter the monthly sales: $") # monthly sales amount
    storeAmount = calcStoreBonus(monthlySales) #store bonus amount
    salesIncrease = getIncrease("Enter percent of sales increase: ") # employee bonus amount
    empAmount = calcEmpBonus(salesIncrease) # percent of sales increase
    printBonus(storeAmount, empAmount)

# gets the monthly sales
def getSales(prompt):
    monthlySales = float(input(prompt))
    return monthlySales

# determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else: 
        storeAmount = 0
    return storeAmount

# gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100
    return salesIncrease

# determines the empAmount bonus
def calcEmpBonus (salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print("Congrats! You have reached the highest bonus amounts possible! ")

main()