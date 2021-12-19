from  employee_wage import EmployeeWageCalculator
from  custom_exception import WrongInputException


class EmployeeBuilder(EmployeeWageCalculator):
    """
    using instance variable instead of function parameter
    storing daily wage of the employee
    searching and displaying monthly employee wage by company  name
    """
    employee_details_list = []

    def add_employee_details(self , employee):
        """
            desc: to add the details in a list 
            param: employee instance variable
            return: no return
        """
        self.employee_details_list.append(employee)

    def query_by_company_name(self ):
        """
            desc: to print the Details by Searching with company name
            param: employee_details_list
            return: no return
        """
        company_name = input("enter the company name : ")
        count = 0
        for i in range(len(self.employee_details_list)):
            if company_name.lower() == (self.employee_details_list[i].company):
                print("Monthly salary : "+str(self.employee_details_list[i].salary))
                count = count + 1
                break
        if count == 0:
            raise WrongInputException("please enter valid company name")

    def display_details(self):
        """
        display  company name , daily wage and total wage of employees
        """
        print(f"{self.employee_details_list[0]}  " + f"{self.employee_details_list[1]}")


employee1 = EmployeeBuilder("amazon", 23, 25, 90)
employee1.calculate_emp_wage()
employee1.add_employee_details(employee1)
employee2 = EmployeeBuilder("flipkart", 22, 24, 80)
employee2.calculate_emp_wage()
employee2.add_employee_details(employee2)
employee2.display_details()

try:
    employee2.query_by_company_name()
except WrongInputException as exception :
    print (exception)