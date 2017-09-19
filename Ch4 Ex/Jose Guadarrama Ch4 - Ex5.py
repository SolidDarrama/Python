# Jose Guadarrama

#user input / per year
totalyears = int(input('Enter the amount of years: '))

#amount of rainfall per month/year
for years in range(totalyears):
    total = 0.0
    print('\nYear', years + 1)
    print('----------------')
    for month in ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'):
        inches = float(input(month))
        total += inches

totalinches = total
totalmonth = totalyears * 12
averinches = total / totalmonth

# print statement
print('\nThe total number of months is: ', totalmonth)
print('The total inches of rainfall is: ', totalinches)
print('The average rainfall per month for the entire period is: ', (format(averinches, ',.2f')))

