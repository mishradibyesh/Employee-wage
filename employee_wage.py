"""
Developing employee Wage Computation Application.
calculating daily wage for a employee till a certain condition
implementing object-oriented paradigm
"""
import random


class EmployeeWage:
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    WAGE_PER_HOUR = 20
    TOTAL_WORKING_DAY = 20
    TOTAL_WORKING_HOURS = 100
    employee_hour = 0
    total_employee_hour = 0
    working_day = 0
    salary = 0

    def calculate_emp_wage(self):
        while self.working_day < self.TOTAL_WORKING_DAY and self.total_employee_hour <= self.TOTAL_WORKING_HOURS:
            self.working_day += 1
            emp_type = random.randint(0, 3)
            if emp_type == 1:
                self.employee_hour = self.FULL_TIME_HOUR
                print(f"on day {self.working_day} Employee is Full time ")
            elif emp_type == 2:
                employee_hour = self.PART_TIME_HOUR
                print(f"on day {self.working_day} Employee is Part time ")
            else:
                print(f"on day {self.working_day} Employee is absent ")
                employee_hour = 0
                self.total_employee_hour += self.employee_hour
            if self.total_employee_hour > self.TOTAL_WORKING_HOURS:
                self.total_employee_hour -= self.employee_hour
                break
        salary = self.WAGE_PER_HOUR * self.total_employee_hour
        print(f"Monthly Income is {salary}")
        print(f"Total working Hours is {self.total_employee_hour}")


employee1 = EmployeeWage()
employee1.calculate_emp_wage()