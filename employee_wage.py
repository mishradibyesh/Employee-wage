"""
Developing employee Wage Computation Application.
calculating daily wage if employee is present
"""
import random
is_present = random.randint(0,2)
salary = 0
if is_present == 1:
	full_day_hour = 8
	wage_per_hour = 20
	salary = salary + (wage_per_hour * full_day_hour)
	print(f"Employee is present and his today's income is {salary}")
else:
	print(f"Employee is absent and  his today's income is {salary}")