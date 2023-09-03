# 7)B) Write a python program by creating a class called Employee to store the 
# details of Name, Employee_ID, Department and Salary, and implement a 
# method to update salary of employees belonging to a given department.

class Employee:
 def __init__(self, name, employee_id, department, salary):
    self.name = name
    self.employee_id = employee_id
    self.department = department
    self.salary = salary
 def update_salary_by_department(self, department, new_salary):
   if self.department == department:
      self.salary = new_salary

employees = [
 Employee('Alice', 'E123', 'Sales', 50000),
 Employee('Bob', 'E456', 'IT', 60000),
 Employee('Charlie', 'E789', 'Sales', 55000),
 Employee('David', 'E012', 'IT', 65000)
]

print("The existing Salaries : ")
for employee in employees:
 print(f'{employee.name} ({employee.department}): ${employee.salary:,}')
print("\n")

department = input('Enter the department: ')
new_salary = int(input('Enter the new salary: '))

for employee in employees:
 employee.update_salary_by_department(department, new_salary)

print("The updated Salaries : ")
for employee in employees:
 print(f'{employee.name} ({employee.department}): ${employee.salary:,}')
