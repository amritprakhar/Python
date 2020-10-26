#Input the data
work_hours=[('Amrit',100),('Billy',200),('Rohit',9999)]
#
def employee_check(work_hours):
	current_max=0
	employee_of_the_month=''
	for employee,hours in work_hours:
		if hours>current_max:
			current_max=hours
			employee_of_the_month=employee
		else:
			pass
	return(employee_of_the_month,current_max)
#Time to check your code

employee_check(work_hours)
