# Jose Guadarrama

keepgoing = 'y'

while keepgoing == 'y' or keepgoing == 'Y':
    C=float(input('Enter the Celsus Degree: '))
    F=C*(9/5)+32
    print('Fahrentheit: ',F)
    keepgoing = input('Do you want to enter another temperature commission (Enter y for yes): ')

print('end of program')