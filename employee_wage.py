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

    def calculate_emp_wage(self, *employee_data):
        total_employee_hour = 0
        working_day = 0
        while working_day < employee_data[2] and total_employee_hour <= employee_data[3]:
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
            if total_employee_hour > employee_data[3]:
                total_employee_hour -= employee_hour
                break
        salary = employee_data[1] * total_employee_hour
        print(f"Monthly Income is {salary}")
        print(f"Total working Hours is {total_employee_hour}")
        employee_data_list = [salary , employee_data[0]]
        return employee_data_list

    def print_details(self, *data):
        print(f"Employee of {data[0][1]} is earning monthly {data[0][0]}")


employee1 = EmployeeWage()
data_list = employee1.calculate_emp_wage("amazon", 23, 25, 90)
employee1.print_details(data_list)
employee2 = EmployeeWage()
data_list = employee2.calculate_emp_wage("flipkart" , 22 , 24 , 80)
employee2.print_details(data_list)

