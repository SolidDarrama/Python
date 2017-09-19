__author__ = 'Josa G and Charles Carper'
# Constants for the menu choices
ADD = 1
SUBTRACT = 2
MULTIPLY = 3
DIVIDE = 4
QUIT_CHOICE = 5
# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    # display the menu.
    display_menu()
    while choice != QUIT_CHOICE:


        # Get the user's choice.
        choice = int(input('\nWhat type of operation would you like to perform? '))

        # Perform the selected action.
        if choice == ADD:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, '+', num2, '=', num1+num2)
        elif choice == SUBTRACT:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, '-', num2, '=', num1-num2)
        elif choice == MULTIPLY:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, '*', num2, '=', num1*num2)
        elif choice == DIVIDE:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, '/', num2, '=', num1/num2)
        elif choice == QUIT_CHOICE:
            print('\n   Thank you for using the Calc Program.\n   Program ended')

        else:
            print('Error: invalid selection.')

# The display_menu function displays a menu.
def display_menu():
    print('Calculations Results')
    print('   1) Add')
    print('   2) Subtract')
    print('   3) Multiply')
    print('   4) Divide')
    print('   5) Quit')

# Call the main function.
main()