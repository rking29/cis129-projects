# Rachel King
# 03/11/25
# tracks the number of bottles returned over 7 days and calculates the total payout based on number of bottles

# declaring variables and intializing the main loop control variable
today_bottles = 0
total_payout = 0
keep_going = "y"
NBR_OF_DAYS = 7

# main loop that can reset the weekly totals
while keep_going == "y":
    total_bottles = 0
    counter = 1

    # collects bottle data for 7 days
    while counter <= NBR_OF_DAYS:
        today_bottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        total_bottles = total_bottles + today_bottles
        counter = counter + 1

    # calculates total payout for the 7 days
    PAYOUT_PER_BOTTLE = .10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    # display results to the user
    print("Total bottles collected:", total_bottles)
    print(f"Total payout: ${total_payout:.1f}")

    # asks user if they would like to enter another week of data
    keep_going = input("Do you want to enter another week’s worth of data? \n(Enter y or n) ").lower()
    