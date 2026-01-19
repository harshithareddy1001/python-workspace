class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def display(self):
        print("Employee Details")
        print("ID:", self.__emp_id)
        print("Name:", self.__name)
        print("Salary:", self.__salary)
class manager(Employee):
   
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary) 
        self.department = department

    def display_manager(self):
        self.display()  
        print("Department:", self.department)
emp1 = Employee(101, "Harshitha", 50000)
emp1.display()

print()

mgr1 = manager(201, "Vaishnavi", 100000, "HR")
mgr1.display_manager()
