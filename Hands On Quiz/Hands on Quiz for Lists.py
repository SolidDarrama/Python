# Jose Guadarrama
#10/22/2014

#create the list
list = ['eggs', 'bacon', 'homefries', 'jelly', 'coffee']

#printed statement
print('Your items:')

#print list
for item in list:
    print(item)

#print Statement + # of items in list
print('\nbreakfast has', len(list), 'items')

#add two more items to the list
list = list + ['orange juice', ' toast']

#print Statement + new # of items in list
print('breakfast now has', len(list), 'items')

#print statement
print('I need some jelly for my toast')

#remove the unwanted item from the list
list.remove('homefries')

#print Statement + final # of items in list
print('breakfast now has', len(list), 'items')

#print the items within the list
print('\nThe complete contents are:', set(list),'\n')

#open txt file
BKi = open('Breakfastitems.txt', 'w')

#write the list to the txt
BKi.write(str(list))

#close txt
BKi.close()

#open txt
BKi2 = open('Breakfastitems.txt', 'r')

#read the txt
lines =BKi2.readlines()

#stripe each line from txt
for i in range(len(lines)):
     lines[i] = lines[i].rstrip('\n')

#close txt again
BKi2.close()

#-------------------------------------------------
#create a two dimensional list
def main():
    #print statement
    print('   List1        List2')

    #Input the info in the list
    List1 = [['Batman', ' Robin'],['Bevis', '  Butthead'],['Shaggy',' Scooby'],['Chip','   Dale'],['Tom','   Jerry']]

    #print the list
    for Names in List1:
        print (Names)

main()