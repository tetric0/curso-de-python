"""
Función que recibe una cantidad variable de precios de
productos y calcula el precio final de todos ellos
aplicando, de forma opcional, un descuento si se
especifica como argumento con nombre.

@params    *args       Lista indeterminada de precios de productos
@params    **kwargs    Descuento (opcional --> por defecto = 0)

@return    float
"""
def calcular_total(*args, **kwargs):
    precio_total = sum(args)

    descuento = kwargs.get('descuento', 0)
    importe_a_descontar = precio_total * descuento / 100

    return precio_total - importe_a_descontar

print('Total artículos (Sin descuento):', calcular_total(39.90, 15.50, 6.15, 57.30, 1.15))
print('Total artículos (10% descuento):', calcular_total(39.90, 15.50, 6.15, 57.30, 1.15, descuento = 10.0))
print('Total artículos (25% descuento):', calcular_total(39.90, 15.50, 6.15, 57.30, 1.15, descuento = 25.0))
print('Total artículos (50% descuento):', calcular_total(39.90, 15.50, 6.15, 57.30, 1.15, descuento = 50.0))