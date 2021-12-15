"""
Developing employee Wage Computation Application.
calculating daily wage for a employee till a certain condition
"""
import random

salary = 0
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4
WAGE_PER_HOUR = 20
employee_hour = 0
TOTAL_WORKING_DAY = 20
TOTAL_WORKING_HOURS = 100
total_employee_hour = 0
working_day = 0
while working_day < TOTAL_WORKING_DAY and total_employee_hour <= TOTAL_WORKING_HOURS:
    working_day += 1
    emp_type = random.randint(0, 3)
    if emp_type == 1:
        employee_hour = FULL_TIME_HOUR
        print(f"on day {working_day} Employee is Full time ")
    elif emp_type == 2:
        employee_hour = PART_TIME_HOUR
        print(f"on day {working_day} Employee is Part time ")
    else:
        print(f"on day {working_day} Employee is absent ")
        employee_hour = 0
    total_employee_hour += employee_hour
    if total_employee_hour > 100:
        total_employee_hour -= employee_hour
        break
salary = WAGE_PER_HOUR * total_employee_hour
print(f"Monthly Income is {salary}")
print(f"Total working Hours is {total_employee_hour}")

