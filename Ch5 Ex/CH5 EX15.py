# Jose Guadarrama

#assign , variable
_list = []
x=0;
def calc_average(total):
    return total / 5

#Grade % to Grade letter
def determine_grade(grade):
    if grade >= 90 and grade <= 100:
        return 'A'
    elif grade >= 80 and grade <= 89:
        return 'B'
    elif grade >= 70 and grade <= 79:
        return 'C'
    elif grade >= 60 and grade <= 69:
        return 'D'
    else:
        return 'F'

#loop
while True:
    x+=1
    print('Enter test score',x,':');
    grade = int(input())
    _list.append(grade)
    avg = calc_average(sum(_list))
    letter = ' '.join([determine_grade(mark) for mark in _list])
    if len(_list) > 4:
        break

#print
print('Average grade: ', avg)
print('Letter grades: ', letter)