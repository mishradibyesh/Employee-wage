"""
Developing employee Wage Computation Application.
calculating daily wage for a employee till a certain condition
implementing object-oriented paradigm
finding wages of employees from different companies
"""
import random


class EmployeeWage:
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    wage_per_hour = 20
    total_working_day = 20
    total_working_hours = 100

    def calculate_emp_wage(self , company , wage_per_hour , total_working_day , total_working_hours ):
        total_employee_hour = 0
        working_day = 0
        self.total_working_hours = total_working_hours
        self.total_working_day = total_working_day
        self.wage_per_hour = wage_per_hour
        while working_day < self.total_working_day and total_employee_hour <= self.total_working_hours:
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
            if total_employee_hour > self.total_working_hours:
                total_employee_hour -= employee_hour
                break
        salary = self.wage_per_hour * total_employee_hour
        print(f"Monthly Income is {salary}")
        print(f"Total working Hours is {total_employee_hour}")
        employee_data_list = [salary , company]
        return employee_data_list

    def print_details(self, *data):
        print(f"Employee of {data[0][1]} is earning monthly {data[0][0]}")


employee1 = EmployeeWage()
data_list = employee1.calculate_emp_wage("amazon" , 23 , 25 , 90)
employee1.print_details(data_list)
employee2 = EmployeeWage()
data_list = employee2.calculate_emp_wage("flipkart" , 22 , 24 , 80)
employee2.print_details(data_list)

