#Jose Guadarrama
#9/15/2014

hourly_rate=0
ot_rate=0
reg_hours_worked=0
ot_hours_worked=0
weekly_pay=0
monthly_pay=0
yearly_pay=0
fname=0
lname=0
totalhrs=0

#user name input
fname=str(input('Enter Your First Name:'))
lname=str(input('Enter Your Last Name:'))

#user hourly rate input
hourly_rate=float(input('Enter Your Hourly Rate:'))

#user work hours
reg_hours_worked=int(input('Enter Your Regular Hours of Work:'))
ot_hours_worked=int(input('Enter Your Over Time Hours of Work:'))
totalhrs=reg_hours_worked+ot_hours_worked

#user over time amount input
ot_rate=ot_hours_worked*(hourly_rate*1.5)

#user pay input
weekly_pay=(hourly_rate*reg_hours_worked)+ot_rate
monthly_pay=weekly_pay*4
yearly_pay=monthly_pay*12

#print statements
print('\nSalary Summary for',lname,', ',fname)

print('\nTotal Hours Worked:\tHourly Rate:\tOvertime Rate:\tWeekly Salary:\tMonthly Salary:\tYearly Salary:')
print(totalhrs,'\t\t\t$',hourly_rate,'\t\t$',ot_rate,'\t$',weekly_pay,'\t$',monthly_pay,'\t$',yearly_pay)
