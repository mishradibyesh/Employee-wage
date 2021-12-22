from custom_exception import WrongInputException


class Company:
    """
    initiating the class members by init method
    using instance variable instead of function parameter
    storing daily wage of the employee
    searching and displaying monthly employee wage by company  name
    """
    employee_details_list = []

    def __init__(self, company, wage_per_hour, total_working_day, total_working_hours):
        self.company = company
        self.wage_per_hour = wage_per_hour
        self.total_working_day = total_working_day
        self.total_working_hours = total_working_hours

    def add_employee_details(self, employee):
        """
            desc: to add the details in a list 
            param: employee instance variable
            return: no return
        """
        self.employee_details_list.append(employee)

    def query_by_company_name(self):
        """
            desc: to print the Details by Searching with company name
            param: employee_details_list
            return: no return
        """
        company_name = input("enter the company name : ")
        count = 0
        for i in range(len(self.employee_details_list)):
            if company_name.lower() == self.employee_details_list[i].company:
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
