class employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def display(self):
        print("employee details")
        print(self.emp_id)
        print(self.name)
        print(self.salary)
emp1=employee(101,"Harshitha",50000)
#print(emp1.emp_id,emp1.name,emp1.salary)
emp1.display()
emp2=employee(102,"vaishnavi",100000)
emp2.display()
employee_directory = {} # Initialize an empty dictionary
emps=[emp1,emp2]
emp3=employee(103, "chinmayi", 60000)



found = False

for emp in emps:
    if emp.emp_id == emp3.emp_id:
        found = True
        break

if not found:
    emps.append(emp3)

    
for items in emps:
    print(items.display())
