from  employee_wage import EmployeeWage
from  custom_exception import WrongInputException


class EmployeeBuilder(EmployeeWage):
    """
    using instance variable instead of function parameter
    storing daily wage of the employee
    searching and displaying monthly employee wage by company  name
    """

    def query_by_company_name(self , employee_details_list):
        """
            desc: to print the Details by Searching with company name
            param: employee_details_list
            return: no return
        """
        self.employee_details_list = employee_details_list
        company_name = input("enter the company name : ")
        count = 0
        for i in range(len(employee_details_list)):
            if company_name.lower() == (self.employee_details_list[i].company):
                print("Monthly salary : "+str(employee_details_list[i].salary))
                count = count + 1
                break
        if count == 0:
            raise WrongInputException("please enter valid company name")


employee1 = EmployeeBuilder("amazon", 23, 25, 90)
employee1.calculate_emp_wage()
employee2 = EmployeeBuilder("flipkart", 22, 24, 80)
employee2.calculate_emp_wage()
employee_details_list = []
employee_details_list.append(employee1)
employee_details_list.append(employee2)
print(f"{employee_details_list[0]}  " + f"{employee_details_list[1]}")
try:
    employee2.query_by_company_name(employee_details_list)
except WrongInputException as exception :
    print (exception)