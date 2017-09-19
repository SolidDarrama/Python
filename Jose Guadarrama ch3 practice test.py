#Jose Guadarrama
#9/15/2014
#salary_amount.py

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
#variables added #2
overtimehrs=0

#user name input
fname=str(input('Enter Your First Name:'))
lname=str(input('Enter Your Last Name:'))

#user hourly rate input
hourly_rate=float(input('Enter Your Hourly Rate:'))

#user work hours
reg_hours_worked=int(input('Enter Your Hours of Work:'))
#if else statement
if reg_hours_worked > 40:
    overtimehrs=reg_hours_worked - 40
    ot_rate=overtimehrs*(hourly_rate*1.5)
    weekly_pay=ot_rate + (40 *hourly_rate)
else:
    weekly_pay=reg_hours_worked*hourly_rate


totalhrs=reg_hours_worked+ot_hours_worked

#user pay input
monthly_pay=weekly_pay*4
yearly_pay=monthly_pay*12

#print statements
print('\nSalary Summary for',lname,', ',fname)

print('\nTotal Hours Worked:\t\tHourly Rate:\tOvertime Rate:\t\tWeekly Salary:\t\tMonthly Salary:\t\tYearly Salary:')
print(totalhrs,'\t\t\t\t\t\t$',(format(hourly_rate, ',.2f')),'\t\t\t$',(format(ot_rate, ',.2f')),'\t\t\t\t$',(format(weekly_pay, ',.2f')),'\t\t\t$',(format(monthly_pay, ',.2f')),'\t\t\t$',(format(yearly_pay, ',.2f')))
