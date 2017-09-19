#Jose Guadarrama
#10/29/2014
#World Series Winners (Use the WorldSeriers.txt file)

#starting point (year)
FIRST_YEAR = 1903

def main():

    #dictonaries
    DICT1 = {}
    DICT2 = {}

    #open txt
    input_file = open('WorldSeries.txt','r')

    #read txt
    LINES = input_file.readlines()

    #strip txt
    for i in range(len(LINES)):
        TEAM = LINES[i].rstrip('\n')

        #if elif statement - to check team winner per year
        Entered_Year = FIRST_YEAR + i
        if Entered_Year >= 1904:
            Entered_Year += 1
        elif Entered_Year >= 1994:
            Entered_Year += 1

        #add updated info to dictionary 1
        DICT1[str(Entered_Year)] = TEAM

        if TEAM in DICT2:
            DICT2[TEAM] += 1
        else:
            DICT2[TEAM] = 1

    #users input
    Entered_Year = input('Enter a year: ')

    #printed statements
    if Entered_Year < '1903' or Entered_Year > '2009':
        print('ERROR; must be a year between 1903-2009')
    elif Entered_Year == '1904' or Entered_Year == '1994':
        print("This year wasn't played")
    else:
        winner = DICT1[Entered_Year]
        wins = DICT2[winner]
        print('\nTeam Winner:', winner,'\nNumber of wins:',wins,)


main()