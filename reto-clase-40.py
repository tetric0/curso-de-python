employees = [
    {
        'name': 'Javier',
        'age': 35,
        'salary': 2400
    },
    {
        'name': 'Víctor',
        'age': 47,
        'salary': 2100
    },
    {
        'name': 'Sergio',
        'age': 50,
        'salary': 2800
    },
    {
        'name': 'Mari Luz',
        'age': 46,
        'salary': 1800
    },
    {
        'name': 'Pedro',
        'age': 54,
        'salary': 2900
    },
]

def get_employees_with_salary_bigger_than():
    '''
    Devuelve la lista de empleados que cobren m´as del sueldo de referencia especificado
    '''
    target_employees = []

    ref_salary = int(input("\nDefine un salario de referencia: "))

    for employee in employees:
        if employee["salary"] > ref_salary:
            target_employees.append(employee)

    print(f"\nLos empleados que cobran más de {ref_salary} son:\n")

    for employee in target_employees:
        print(f"    > {employee['name']}\t{employee['age']} años\t(Salario: {employee['salary']})")

print("\nLista de empleados:\n")

for employee in employees:
    print(f"    > {employee['name']}\t{employee['age']} años\t(Salario: {employee['salary']})")

get_employees_with_salary_bigger_than()