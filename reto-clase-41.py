from typing import Union

class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

employee_1 = Employee("Javier", 35, 2400.50)
employee_2 = Employee("Víctor", 47, 2100.00)
employee_3 = Employee("Sergio", 50, 2800.75)
employee_4 = Employee("Mari Luz", 46, 1800.35)
employee_5 = Employee("Pedro", 54, 2900.99)

employees = [employee_1, employee_2, employee_3, employee_4, employee_5]

def get_employees_with_salary_bigger_than(employees: list[Employee], ref_salary: float):
    '''
    Devuelve la lista de empleados que cobren más del sueldo de referencia especificado
    '''
    target_employees = []

    for employee in employees:
        if employee.salary > ref_salary:
            target_employees.append(employee)
    
    return target_employees

print("\nLista de empleados:\n")

for employee in employees:
    print(f"    > {employee.name}\t{employee.age} años\t(Salario: {employee.salary})")

ref_salary = float(input("\nDefine un salario de referencia: "))

print(f"\nLos empleados que cobran más de {ref_salary} son:\n")

for employee in get_employees_with_salary_bigger_than(employees, ref_salary):
    print(f"    > {employee.name}\t{employee.age} años\t(Salario: {employee.salary})")

