#Jose Guadarrama
#10/21/2014

#tupple
key_pad = \
   [("ABC", "2"),
    ("DEF", "3"),
    ("GHI", "4"),
    ("JKL", "5"),
    ("MNO", "6"),
    ("PQRS","7"),
    ("TUV", "8"),
    ("WXYZ","9")]

#defining
def CharNum(letter):
    for i in key_pad:
        if letter in i[0]:
            return i[1]
    return letter

#asking user's input
UserInput=input('Enter 10-Character Telephone number [Format XXX-XXX-XXXX]: ')
#upper casing (just in case, lower case letters are entered)
UserInput = UserInput.upper()
final=''
x=0

#while loop
while x < len(UserInput):
    #placing the # in order
    final += CharNum(UserInput[x])
    #continuing the loop
    x+=1

#print statement
print('\n',final)