#Jose Guadarrama
#9/20/2014
#CH3 EX10

total = 1

#user input 1
NUMpennies=float(input('Enter the number of pennies: '))
NUMnickels=float(input('Enter the number of nickels: '))
NUMdimes=float(input('Enter the number of dimes: '))
NUMquarters=float(input('Enter the number of quarters: '))

#curreny amount
pennies = NUMpennies * .01
nickles = NUMnickels * .05
dimes = NUMdimes * .10
quarters = NUMquarters * .25


#print statement
if total == pennies + nickles + dimes + quarters:
    print('\nCongratulation')

elif total > pennies + nickles + dimes + quarters:
    print('\nAmount input is less than a dollar')

elif total < pennies + nickles + dimes + quarters:
    print('\nAmount input is more than a dollar')

input()