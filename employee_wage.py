"""
Developing employee Wage Computation Application.
"""
import random
from employee_builder import Company


class EmployeeWageCalculator(Company):
    """
    calculating daily wage for a employee till a certain condition
    implementing object-oriented paradigm
    finding wages of employees from different companies :
    ability to manage employee wage of multiple companies
    """
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    total_employee_hour = 0
    working_day = 0

    def calculate_emp_wage(self):
        """
            desc: calculate daily wages and monthly wages of employee
            param: emp_check:
            return: employee hour(int value)
        """
        self.daily_wage_list = []   
        while self.working_day < self.total_working_day and self.total_employee_hour <= self.total_working_hours:
            self.working_day += 1
            emp_type = random.randint(0, 2)
            if emp_type == 1:
                employee_hour = self.FULL_TIME_HOUR
            elif emp_type == 2:
                employee_hour = self.PART_TIME_HOUR
            else:
                employee_hour = 0
            self.total_employee_hour += employee_hour
            if self.total_employee_hour > self.total_working_hours:
                self.total_employee_hour -= employee_hour
                break
            self.daily_wage = self.wage_per_hour * employee_hour
            self.daily_wage_list.append(self.daily_wage)
        self.salary = self.wage_per_hour * self.total_employee_hour

    def __str__(self):
        """
        overriding __str__ method to return company name ,daily wage and monthly wage
        """
        return "\n" + "Company Name : " + self.company + ", DailyWage:" + str(
            self.daily_wage_list) + "  " + " , Monthly wage : " + str(self.salary)


employee1 = EmployeeWageCalculator("amazon", 23, 25, 90)
employee1.calculate_emp_wage()
employee1.add_employee_details(employee1)
employee2 = EmployeeWageCalculator("flipkart", 22, 24, 80)
employee2.calculate_emp_wage()
employee2.add_employee_details(employee2)
employee2.display_details()

try:
    employee2.query_by_company_name()
except WrongInputException as exception:
    print(exception)