#Jose Guadarrama
#10.8.2014

import random
count=0

#open txt
file = open('ex7', 'w')

#user input
num_want=int(input('How many random numbers will there be? '))

#the amount if numbers requested by user
for count in range(1, num_want + 1):
    #random numbers
    num=random.randint(1, 500)
    #random number written in the file
    file.write(str(num) + '\n')

#close txt
file.close()
