#Jose Guadarrama
#10-13-2014

#variable with value that controls the number of inputs from user
NUM = 20

def main():

    #Value given to variables
    number = [0] * NUM
    index=0
    count=0
    total=0
    count_num=0
    avg=0

    #While loop
    while index < NUM:
        #To count the number of inputs
        count += 1
        #ask user to input numbers
        print('Please enter number(Slot',count,'):')
        number[index] = float(input())
        #index helps to keep track, so it will only ask the user 20 times
        index += 1

    #for loop
    for value in number:
        #the numbers the user entered, are add together
        total+=value
        count_num += 1

    #average
    avg = total/count_num

    #print statements
    print('\nLowest Value Number is :',min(number))
    print('Highest Value Number is :',max(number))
    print('Total:',total)
    print('Average:',avg)

main()