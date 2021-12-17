"""
Developing employee Wage Computation Application.
calculating daily wage for a employee till a certain condition
implementing object-oriented paradigm
finding wages of employees from different companies
using instance variable instead of function parameter
"""
import random


class EmployeeWage:
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4

    def __init__(self, *employee_data):
        total_employee_hour = 0
        working_day = 0
        company = employee_data[0]
        wage_per_hour = employee_data[1]
        total_working_day = employee_data[2]
        total_working_hours = employee_data[3]
        while working_day < total_working_day and total_employee_hour <= total_working_hours:
            working_day += 1
            emp_type = random.randint(0, 3)
            if emp_type == 1:
                employee_hour = self.FULL_TIME_HOUR
                print(f"on day {working_day} Employee is Full time ")
            elif emp_type == 2:
                employee_hour = self.PART_TIME_HOUR
                print(f"on day {working_day} Employee is Part time ")
            else:
                print(f"on day {working_day} Employee is absent ")
                employee_hour = 0
            total_employee_hour += employee_hour
            if total_employee_hour > total_working_hours:
                total_employee_hour -= employee_hour
                break
        salary = wage_per_hour * total_employee_hour
        print(f"Monthly Income is {salary}")
        print(f"Total working Hours is {total_employee_hour}")
        self.print_details(company,salary)

    def print_details(self,company,salary):
        print(f"Employee of {company} is earning monthly {salary}")


employee1 = EmployeeWage("amazon", 23, 25, 90)
employee2 = EmployeeWage("Flipkart", 22, 24, 80)


