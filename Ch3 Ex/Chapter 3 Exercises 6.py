#Jose Guadarrama
#9/20/2014

month=0
day=0
year=0


#user date input
month=float(input('Enter a month (Numeric Form):'))
day=float(input('Enter a day:'))
year=float(input('Enter a two-digit year:'))

#if else statement
if year==month*day:
    print('\nThe date is magic')

else:
    print('\nThe date is not magic')

input()
