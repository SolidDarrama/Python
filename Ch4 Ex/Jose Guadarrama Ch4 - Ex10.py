# Jose Guadarrama

#Declare Variables
semester=8000

for years in range(5):
    print('Year', years + 1)
    increase = 0.03 * (years+1)
    total=(increase*semester) + semester
    print((format(total, ',.2f')),'\n')