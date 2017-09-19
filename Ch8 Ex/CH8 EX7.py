#Jose Guadarrama
#10-21-2014

def main():

    #initializing
    upper_count=0
    lower_count=0
    digit_count=0
    space_count=0

    #open txt
    infile = open('Text.txt','r')
    #reads the lines from txt
    file = infile.readlines()

    #for loop
    for lines in file:
        #for loop - Counting/Searching
        for ch in lines:
            #Counting UpperCase
            if ch.isupper():
                upper_count+=1
            #Counting LowerCase
            elif ch.islower():
                lower_count+=1
            #Counting Digits
            elif ch.isspace():
                digit_count+=1
            #Counting the White Spaces
            elif ch.isdigit():
                space_count+=1

    #Print Statement
    print('Total # of Upper Case Letters:',upper_count)
    print('Total # of Lower Case Letters:',lower_count)
    print('Total # of Digits is:',digit_count)
    print('Total # of White Spaces is:',space_count)

    infile.close()
main()