#declare variable
amountpur=0.00
staterate=0.05
countyrate=0.025
totaltax=0.0
totalsale=0.0

#User intput
amountpur=float(input('Please enter the amount of purchase: '))

#statetax
statetax=amountpur*staterate

#countytax
countytax=amountpur*countyrate

#totaltax
totaltax=statetax+countytax

#Final total sale
totalsale=amountpur+totaltax

#Output Statement
print('Recipe:\n Amount of the Purchase:',amountpur,'\n State Tax:',statetax,'\n County Tax:',countytax,'\n Total Tax:',totaltax,'\n Total Sale',totalsale)




