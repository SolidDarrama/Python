#Jose Guadarrama
#10/15/2014


count=0

#Opens the text file
ChargAcc = open('charge_accounts.txt', 'r')

#ask user account number to be input
userValue=input('Enter Charge Account Number: ')

#reads the lines from text
lines =ChargAcc.readlines()

for i in range(len(lines)):
     lines[i] = lines[i].rstrip('\n')


if userValue not in lines:
    print('Invalid')
else:
    print('Valid')


#close text
ChargAcc.close()