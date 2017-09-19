#Jose Guadarrama
#10/15/2014

def main():

    count=0
    total=0

    #Opens the text file
    WSWin = open('WorldSeriesWinners.txt', 'r')

    #reads the lines from text
    lines =WSWin.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')

    #ask user account number to be input
    userValue=input('Enter Team Name: ')

    if userValue not in lines:
        print('Sorry, they  have not won')

    else:
        for item in lines:
            if item == userValue:
                count += 1
        print('\nThe ',userValue,' has won ', count)

    #print Statement


    #close text
    WSWin.close()

main()