#Jose Guadarrama
#9/20/2014
#CH3 EX7



#user input 1
primary1=str(input('Enter the 1st Primary Color: '))
#if else 1
while primary1 != "red" and primary1 != "blue" and primary1 != "yellow":
    primary1 = input("\nerror message")

#user input 2
primary2=str(input('Enter the 2nd Primary Color: '))
#if else 2
while primary2 != "red" and primary2 != "blue" and primary2 != "yellow":
    primary2 = input("\nerror message")

#color mix equation
if primary1 == 'blue' and primary2 == 'red':
    print('Color Result: Purple')

elif primary1 == 'red' and primary2 == 'blue':
    print('Color Result: Purple')

elif primary1 == 'blue' and primary2 == 'yellow':
    print('Color Result: Green')

elif primary1 == 'yellow' and primary2 == 'blue':
    print('Color Result: Green')

elif primary1 == 'red' and primary2 == 'yellow':
    print('Color Result: Orange')

elif primary1 == 'yellow' and primary2 == 'red':
    print('Color Result: Orange')

input()