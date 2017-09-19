# Jose Guadarrama

#conversion
def main():
    #declare variables
    feet=0.0
    inches=0.0
    foot=0.0

    #get number of feet
    feet=int(input('Enter the number of feet: '))
    #Sends variable 'feet' to the def feet_to_inches
    inches=feet_to_inches(feet)
    #new value comes back, within the variable 'inches' from the above statement
    print('\nThere is',inches, 'inches in',feet,"feet")

#Recieves the value of 'feet' from the line, inches=feet_to_inches(feet)// and places it in a new variable (foot)
def feet_to_inches(foot):
    result = foot * 12
    return result
    #returns the value from the final variable {result}

main()
