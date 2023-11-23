class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        overtime = hours_worked - 50
        if overtime > 0:
            self.emp_salary += overtime * (self.emp_salary / 50)

    def emp_assign_department(self, assign_dp):
        self.emp_department = assign_dp

    def print_employee_details(self):
        print(
            f"Name: {self.emp_name}\nID: {self.emp_id}\nSalary: {self.emp_salary}\nDepartment: {self.emp_department}"
        )


emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

emp1.calculate_emp_salary(60)
emp1.emp_assign_department("TESTING 1")
emp1.print_employee_details()


emp2.calculate_emp_salary(55)
emp2.emp_assign_department("TESTING 2")
emp2.print_employee_details()


emp3.calculate_emp_salary(30)
emp3.emp_assign_department("TESTING 3")
emp3.print_employee_details()


emp4.calculate_emp_salary(90)
emp4.emp_assign_department("TESTING 4")
emp4.print_employee_details()
