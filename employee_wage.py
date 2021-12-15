"""
Developing employee Wage Computation Application.
calculating daily wage if employee is present
"""
import random
salary = 0
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4
WAGE_PER_HOUR = 20
employee_hour = 0
emp_type = random.randint(0,3)
if emp_type == 1:
	employee_hour = FULL_TIME_HOUR
	print("Employee is Full time ")
elif emp_type == 2:
	employee_hour = PART_TIME_HOUR
	print("Employee is Part time ")
else:
	print("Employee is absent ")
	employee_hour = 0
salary = salary + (WAGE_PER_HOUR * employee_hour)
print(f"Income is {salary}")
