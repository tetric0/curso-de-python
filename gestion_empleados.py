class Employee:
    def __init__(self, id:int, nombre:str, apellido:str, edad:int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"{self.id}\t{self.nombre}\t{self.apellido}\t{self.edad} años"
    
    def __repr__(self):
        return f"Persona(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', edad={self.edad})"
    
class GestorEmpleados:
    employees = []

    def add_employee(self, nombre, apellido, edad):
        # Calculamos el ID de la nueva persona (si no hay empleados, será 1)
        new_id = 1
        if len(self.employees) != 0:
            new_id = max(self.employees, key=lambda employee: employee.id).id + 1

        new_employee = Employee(new_id, nombre, apellido, edad)
        self.employees.append(new_employee)

        print(f"Añadido el empleado {new_employee.nombre} {new_employee.apellido}, de {new_employee.edad} años [ID: {new_employee.id}]")
    
    def remove_employee(self, id):
        # Recupero el objeto Employee a borrar, de la lista de empleados (Suponiendo que el ID es único)
        matching_employees = [employee for employee in self.employees if employee.id == id]
        if len(matching_employees) != 0:
            employee_to_delete = matching_employees[0]

        # Borro el empleado de la lista
        self.employees.remove(employee_to_delete)

        #Imprimo el resultado de la operación
        print(f"Borrado el empleado con ID: {employee_to_delete.id} [{employee_to_delete.nombre} {employee_to_delete.apellido}. {employee_to_delete.edad} años]")
    
    def print_current_employees(self):
        print("\nLISTA DE EMPLEADOS")
        print("\nID\tNOMBRE\tAPELLIDO\tEDAD")
        for employee in self.employees:
            print(employee)
        print("\n")

if __name__ == "__main__":
    gestor_1 = GestorEmpleados()

    gestor_1.add_employee("Víctor", "Gutierrez", 47)
    gestor_1.add_employee("Mariluz", "Mansilla", 46)
    gestor_1.add_employee("Víctor", "Mansilla", 38)

    gestor_1.print_current_employees()

    gestor_1.remove_employee(2)

    print("\nLISTA DE EMPLEADOS")
    print("\nID\tNOMBRE\tAPELLIDO\tEDAD")
    for employee in gestor_1.employees:
        print(employee)
    print("\n")

    gestor_1.add_employee("Pedro", "Villanueva", 25)
    gestor_1.add_employee("Julián", "Berategui", 34)

    gestor_1.print_current_employees()