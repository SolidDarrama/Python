#Jose Guadarrama
#10.8.2014


#initializing
count=0
total=0
avg=0

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

#close txt
numberfile.close()

#print
print(avg)
