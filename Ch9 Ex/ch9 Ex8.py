#Jose Guadarrama
#10/31/2014

import pickle

#global menu
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#filename
FILENAME = 'mydatafile.dat'

def main():

    #directory
    Email_Book = load_email()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(Email_Book)
        elif choice == ADD:
            add(Email_Book)
        elif choice == CHANGE:
            change(Email_Book)
        elif choice == DELETE:
            delete(Email_Book)

    #when finished, it saves
    Savefie(Email_Book)

    print('Information Saved')

def load_email():
    #loads the directory file
    try:
        inputfile = open('FILENAME', 'rb')

        email_dict = pickle.load(inputfile)

        inputfile.close()

    except IOError:
        email_dict = {}

    return email_dict


def get_menu_choice():

    #print menu
    print("\nMENU: \n1)Look Up Email Address \n2)Add a New Name & Email Address \n3)Update an Existing Email Address \n4)Delete a Name & Email Address \n5)Quit\n")

    #users input value
    choice = int(input('Enter Your Choice: '))

    #While - QUIT
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))


    return choice

def look_up(Email_Book):
#looks through the directory

    name = input ('Enter a name: ')

    print(Email_Book.get(name, 'Not Found.'))

def add(Email_Book):
#adds name/email to the directory

    name = input ('Enter a name: ')
    email = input ('Enter an email address: ')

    if name not in Email_Book:
        Email_Book[name] = email
    else:
        print('That entry already exists.')


def change(Email_Book):
#changes the info within the directory

    name = input('Enter a name:')

    if name in Email_Book:
        email = input('Enter the new email: ')

        Email_Book[name] = email
    else:
        print('That name is not found.')


def delete(Email_Book):
#deletes name/email from the directory

    name = input('Enter a name: ')

    if name in Email_Book:
        del Email_Book[name]
    else:
        print('That name is not found.')

def Savefie(Email_Book):

    #opens file
    outputfile = open('FILENAME', 'wb')

    #pickle the directory / saves it
    pickle.dump(Email_Book, outputfile)

    #closes file
    outputfile.close()


main()