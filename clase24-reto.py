'''
RETO

Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos.
Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno.
Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.
'''

def fill_with_blank_spaces(final_spaces, filled_spaces):
    response = ""
    for i in range(final_spaces - filled_spaces):
        response += " "
    return response

class Car:
    def __init__(self, id, brand, model, price):
       self.id = id
       self.brand = brand
       self.model = model
       self.price = price
       self.in_stock = True
    
    def sell(self):
        if self.in_stock:
            self.in_stock = False
            print("El {} {} con referencia {} ha sido vendido por {}€".format(self.brand, self.model, self.id, self.price))
        else:
            print("El {} {} con referencia {} no está en stock".format())

class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.owned_cars = []
    
    def buy_car(self, car):
        if car.in_stock:
            car.sell()
            self.owned_cars.append(car)
        else:
            print("El vehículo {} {} con referencia {} ya no está en stock".format(car.brand, car.model, car.id))

class CarDealership:
    def __init__(self):
        self.cars = []
        self.users = []
    
    def add_car(self, car):
        self.cars.append(car)
        print("El concesionario ha adquirido una nueva unidad de {} {}. Su número de referencia es '{}'".format(car.brand, car.model, car.id))
    
    def add_user(self, user):
        self.users.append(user)
        print("El usuario {} ha sido añadido en el sistema".format(user.username))
    
    def show_available_cars(self):
        column_spaces = 20
        print('''
-----------------------------------------------------------------------
CATÁLOGO DE VEHÍCULOS
-----------------------------------------------------------------------
REFERENCIA          MARCA               MODELO              PRECIO
''')
        
        for car in self.cars:
            if car.in_stock:
                print("{}{}{}{}{}{}{}{}".format(
                    car.id, fill_with_blank_spaces(column_spaces, len(car.id)),
                    car.brand, fill_with_blank_spaces(column_spaces, len(car.brand)),
                    car.model, fill_with_blank_spaces(column_spaces, len(car.model)),
                    car.price, fill_with_blank_spaces(column_spaces, len(car.price))
                ))
        
        print('''-----------------------------------------------------------------------
''')

# Creación de vehículos
car1 = Car('V001', 'Dacia', 'Sandero', '21000')
car2 = Car('V002', 'Hyundai', 'Tucson', '17500')
car3 = Car('V003', 'Toyota', 'Corolla', '50000')
car4 = Car('V004', 'Kia', 'Sportage', '18000')
car5 = Car('V005', 'Toyota', 'Yaris Cross', '25000')

# Creación de usuarios
user1 = User('U001', 'victor.munoz')
user2 = User('U002', 'jordi.guillem.fragoso')
user3 = User('U003', 'fermin.santin')

# Creación de concesionario
car_dealership = CarDealership()

car_dealership.add_car(car1)
car_dealership.add_car(car2)
car_dealership.add_car(car3)
car_dealership.add_car(car4)
car_dealership.add_car(car5)

car_dealership.add_user(user1)
car_dealership.add_user(user2)
car_dealership.add_user(user3)

# Mostrar vehículos
car_dealership.show_available_cars()

# Compra de Vehiculos
user1.buy_car(car1)
user2.buy_car(car1)
car_dealership.show_available_cars()
user2.buy_car(car3)
car_dealership.show_available_cars()

car6 = Car('V006', 'SEAT', 'León FR', '27000')
car_dealership.add_car(car6)
car_dealership.show_available_cars()
