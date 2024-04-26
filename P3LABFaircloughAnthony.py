#Anthony Fairclough
#4/26/2024
#Branching / Debugging
# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line.
# I received help from the instructor in the help lab on Friday

change_amount = int(input() )

# create a condition if no change is output
if change_amount <= 0:
    print("No change")
    
# create variable for dollars use remainder for math
dollars = change_amount // 100

# update change_amount and print the number of dollars
if dollars > 0 and change_amount > 0:
    change_amount = change_amount - (dollars * 100)
if dollars == 1:
    print(dollars, 'Dollar')
elif dollars > 1:
    print(dollars, 'Dollars')
    
# create variable for quarters use remainder for math
quarters = change_amount // 25

# Update change_amount and print the number of quarters
if quarters > 0 and change_amount > 0:
    change_amount = change_amount - (quarters * 25)
if quarters == 1:
    print(quarters, 'Quarter')
elif quarters > 1:
    print(quarters, 'Quarters')
    
# create variable for dimes and use remainder for math
dimes = change_amount // 10

# Update change_amount and print the number of dimes
if dimes > 0 and change_amount > 0:
    change_amount = change_amount - (dimes * 10)
if dimes == 1:
    print(dimes, 'Dime')
elif dimes > 1:
    print(dimes, 'Dimes')
    
# Create variable or nickles and use remainder for math
nickles = change_amount // 5


# Update change_amount and print the number of nickles
if nickles > 0 and change_amount > 0:
    change_amount = change_amount - (nickles * 5)
if nickles == 1:
    print(nickles, 'Nickel')
elif nickles > 1:
    print(nickels, 'Nickles')
    
    
# Create variable for pennies and use remainder for math
pennies = change_amount // 1

# Update change_amount and print number of pennies
if pennies > 0 and change_amount > 0:
    change_amount = change_amount - (pennies * 1)
if pennies == 1:
    print(pennies, 'Penny')
elif pennies > 1:
    print(pennies, 'Pennies')


