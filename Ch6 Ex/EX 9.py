#Jose Guadarrama
#10.8.2014

def main():
    #initializing
    count=0
    total=0
    avg=0

    try:
        #open txt
        numberfile = open('numbers.txt', 'r')

        #Get the values per line
        for line in numberfile:
            #convert line to float
            lineZ = float(line)
            #adding 1 to count ;for the average
            count += 1
            #combining every line value into one
            total += lineZ

        #producing the average
        avg = total/count

    except IOError:
        print('Error occurred trying to read the file')

    except ValueError:
        print('Error Non-numeric data found in the file')

        #close txt
        numberfile.close()

        #print
        print(avg)

main()