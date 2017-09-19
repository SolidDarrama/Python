# Jose Guadarrama

#random numbers

import random
num1=random.randint(1, 500)
print(' ',format(num1, ',.0f'))

import random
num2=random.randrange(500)
print("+",(format(num2, ',.0f')))

#combined random numbers
total=num1+num2

#users guess input
userAns=int(input('_____\n  '))

#if else
if userAns==total:
    print("Congratulation")

else:
    print('\nAnswer is ',total)

