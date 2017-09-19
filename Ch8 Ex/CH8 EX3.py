# Jose Guadarrama
#10/21/2014


def main():
    #create a string with a date
    UserInput=input('Enter Date [Format XX/XX/XXXX]: ')

    date_list = UserInput.split('/')

    if date_list[0] == '1':
        print('January',date_list[1],', ',date_list[2])
    elif date_list[0] == '2':
        print('February',date_list[1],', ',date_list[2])
    elif date_list[0] == '3':
        print('March',date_list[1],', ',date_list[2])
    elif date_list[0] == '4':
        print('April',date_list[1],', ',date_list[2])
    elif date_list[0] == '5':
        print('May',date_list[1],', ',date_list[2])
    elif date_list[0] == '6':
        print('June',date_list[1],', ',date_list[2])
    elif date_list[0] == '7':
        print('July',date_list[1],', ',date_list[2])
    elif date_list[0] == '8':
        print('August',date_list[1],', ',date_list[2])
    elif date_list[0] == '9':
        print('September',date_list[1],', ',date_list[2])
    elif date_list[0] == '10':
        print('October',date_list[1],', ',date_list[2])
    elif date_list[0] == '11':
        print('November',date_list[1],', ',date_list[2])
    elif date_list[0] == '12':
        print('December',date_list[1],', ',date_list[2])


main()
