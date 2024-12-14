class Pedido:
    descuento_global = 0  # Descuento global (Por defecto igual a cero)

    def __init__(self, importe):
        self.importe = importe
        self.importe_final = importe - (importe * Pedido.descuento_global / 100)

    @staticmethod
    def verificar_importe_minimo(importe, minimo = 50):
        # Verifica si el importe del pedido es mayor o igual al mínimo permitido.
        return importe >= minimo

    @classmethod
    def crear_con_descuento(cls, importe):
        # Crea un pedido aplicando el descuento global actual.
        if not cls.verificar_importe_minimo(importe):
            raise ValueError("El importe no cumple con el mínimo permitido.")
        return cls(importe)

    @classmethod
    def actualizar_descuento_global(cls, nuevo_descuento):
        # Actualiza el descuento global para todos los pedidos.
        cls.descuento_global = nuevo_descuento
