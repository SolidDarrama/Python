#Billy Leager
#10/1/2014
#Practice Program - Menu

def rectangle_area():
    side1 = int(input('Enter the value of the first side:'))
    side2 = int(input('Enter the value of the second side:'))
    print('The area of the rectangle is', (side1 * side2))

def triangle_area():
    height = int(input('Enter the height of the triangle:'))
    base = int(input('Enter the base of the triangle:'))
    print('The area of the triangle is', ((height * base) / 2))
            
keep_going = input('Choose r to calculate the area of a rectangle or t to calculate the area of a triangle, or q to quit:')

#Creating a while loop to execute the following functions and statements if menu_value does not equal Q.
while keep_going != 'q':
    if keep_going == 'r':
        rectangle_area()
        keep_going = input('Choose r to calculate the area of a rectangle or t to calculate the area of a triangle, or q to quit:')
    elif keep_going == 't':
        triangle_area()
        keep_going = input('Choose r to calculate the area of a rectangle or t to calculate the area of a triangle, or q to quit:')
    else:
        keep_going = 'q'


print('Exiting program')
                
    
