#Jose Guadarrama
#11/10/2014

#create class
class Employee:

    #__init__ initializes the attribute
    def __init__(self, Name, ID_No, Department, Job_Title):
        self.Name = Name
        self.ID_No = ID_No
        self.Department = Department
        self.Job_Title = Job_Title

    #accepts argument
    def __str__(self):
        strings = ('{}'.format(self.Name),'{}'.format(self.ID_No),'{}'.format(self.Department),'{}'.format(self.Job_Title))
        #returns it & joins the data info via " | "
        return '    |   '.join(strings)


def main():

    #employee data /name, id, department, job title
    Name = "Susan Meyers"
    ID_No = "47899"
    Department = "Accounting   "
    Job_Title = "Vice President"
    #all the info, stored into the Employee1 data
    Employee1 = Employee(Name, ID_No, Department, Job_Title)

    Name = "Mark Jones  "
    ID_No = "39119"
    Department = "IT           "
    Job_Title = "Programmer"
    Employee2 = Employee(Name, ID_No, Department, Job_Title)

    Name = "Joy Rogers  "
    ID_No = "81774"
    Department = "Manufacturing"
    Job_Title = "Engineer"
    Employee3 = Employee(Name, ID_No, Department, Job_Title)

    #print each individual employee data
    print('    Name        | ID Number  |    Department      |    Job Title')
    print('-------------------------------------------------------------------')
    print(Employee1)
    print(Employee2)
    print(Employee3)


main()