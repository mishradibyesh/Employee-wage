"""
Developing employee Wage Computation Application.
calculating daily wage for a employee till a certain condition
implementing object-oriented paradigm
finding wages of employees from different companies
using instance variable instead of function parameter
ability to manage employee wage of multiple companies
"""
import random


class EmployeeWage:
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    total_employee_hour = 0
    working_day = 0

    def __init__(self, *employee_data):
        self.company = employee_data[0]
        self.wage_per_hour = employee_data[1]
        self.total_working_day = employee_data[2]
        self.total_working_hours = employee_data[3]
    def calculate_emp_wage(self):
        while self.working_day < self.total_working_day and self.total_employee_hour <= self.total_working_hours:
            self.working_day += 1
            emp_type = random.randint(0, 3)
            if emp_type == 1:
                employee_hour = self.FULL_TIME_HOUR
                print(f"on day {self.working_day} Employee is Full time ")
            elif emp_type == 2:
                employee_hour = self.PART_TIME_HOUR
                print(f"on day {self.working_day} Employee is Part time ")
            else:
                print(f"on day {self.working_day} Employee is absent ")
                employee_hour = 0
            self.total_employee_hour += employee_hour
            if self.total_employee_hour > self.total_working_hours:
                self.total_employee_hour -= employee_hour
                break
        self.salary = self.wage_per_hour * self.total_employee_hour
        print(f"Monthly Income is {self.salary}")
        print(f"Total working Hours is {self.total_employee_hour}")
        self.print_details(self.company,self.salary)

    def print_details(self,company,salary):
        print(f"Employee of {company} is earning monthly  {salary}")

    def __str__(self):
        return self.company + "  " + str(self.salary)


employee1 = EmployeeWage("amazon", 23, 25, 90)
employee1.calculate_emp_wage()
employee2 = EmployeeWage("Flipkart", 22, 24, 80)
employee2.calculate_emp_wage()
employee_detail_list = []
employee_detail_list.append(employee1)
employee_detail_list.append(employee2)
print(f"{employee_detail_list[0]}  " + f"{employee_detail_list[1]}")



