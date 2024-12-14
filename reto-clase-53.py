class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = precio    # Atributo protegido mediante _
        self._stock = stock      # Atributo protegido mediante _
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio de un producto no puede ser negativo")
        self._precio = nuevo_precio
    
    @precio.deleter
    def precio(self):
        del self._precio
        print(f"El precio del producto {self.nombre} ha sido borrado")
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("El stock de un producto no puede ser negativo")
        
        self._stock = nuevo_stock
    
    @stock.deleter
    def stock(self):
        del self._stock
        print(f"El stock del producto {self.nombre} ha sido borrado")
    
    # Método que calcula el valor total del producto en el inventario
    # stock * precio
    def valor_total_en_inventario (self):
        return self._stock * self._precio
    
def listar_inventario():
    print("===========================================================================================================================")
    print("INVENTARIO")
    print("===========================================================================================================================")
    print("ARTÍCULO\t\t\tPRECIO UNITARIO\t\t\tCANTIDAD\t\t\tPRECIO EN INVENTARIO")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(f"{producto1.nombre}\t\t\t{producto1.precio}\t\t\t\t{producto1.stock}\t\t\t\t{producto1.valor_total_en_inventario()}")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(f"{producto2.nombre}\t\t\t{producto2.precio}\t\t\t\t{producto2.stock}\t\t\t\t{producto2.valor_total_en_inventario()}")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(f"{producto3.nombre}\t\t\t{producto3.precio}\t\t\t\t{producto3.stock}\t\t\t\t{producto3.valor_total_en_inventario()}")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(f"{producto4.nombre}\t\t\t{producto4.precio}\t\t\t\t{producto4.stock}\t\t\t\t{producto4.valor_total_en_inventario()}")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(f"{producto5.nombre}\t\t\t{producto5.precio}\t\t\t\t{producto5.stock}\t\t\t\t{producto5.valor_total_en_inventario()}")   
    print("===========================================================================================================================")


# PRUEBAS
producto1 = Producto("Pegamento", 0, 0)
producto2 = Producto("Destornillador", 0, 0)
producto3 = Producto("Alicates", 0, 0)
producto4 = Producto("Lijadora", 0, 0)
producto5 = Producto("Linterna", 0, 0)


## Getters
listar_inventario()

## Setters
producto1.precio = 6
producto1.stock = 50
producto2.precio = 12
producto2.stock = 80
<<<<<<< HEAD
producto3.precio = 20
=======
producto3.precio =20
>>>>>>> 291ff522611c0674cb364805bbc6a790c5db1433
producto3.stock = 77
producto4.precio = 54
producto4.stock = 10
producto5.precio = 27
producto5.stock = 8
listar_inventario()

## Control de precio y stock negativo
# producto1.precio = -1
# producto1.stock = -75
# listar_inventario()


## Deleter
del producto3.precio
del producto5.stock