from collections import Counter, defaultdict, deque
from enum import Enum

# Enumeración para definir los estados de un pedido
class OrderStatus(Enum):
    PENDING = 1       # Pendiente
    SHIPPED = 2       # Enviado
    DELIVERED = 3     # Entregado

# Clase para representar un pedido
class Order:
    def __init__(self, id: int, status: OrderStatus = OrderStatus.PENDING) -> None:
        self.id = id
        self.status = status
    
    def get_status(self):
        # print(f"status: {self.status}")
        # print(f"status.name: {self.status.name}")
        # print(f"status.value: {self.status.value}")
        match self.status:
            case OrderStatus.PENDING:
                return "Pendiente de envío"
            case OrderStatus.SHIPPED:
                return "Enviado"
            case OrderStatus.DELIVERED:
                return "Entregado"
    
    def __repr__(self) -> str:
        return f"Pedido #{self.id} [{self.get_status()}]"

# Clase para representar el gestor de pedidos
class OrderManager:
    def __init__(self, orders_queue: deque[Order] = deque(), orders: list[Order] = {}) -> None:
        # Cola de pedidos por orden de llegada
        self.orders_queue = orders_queue

        # Cola de pedidos por ID
        self.orders = orders
    
    # Agrega un nuevo pedido en estado pendiente de envío
    def add_order(self, order_id: int):
        order = Order(order_id)
        self.orders_queue.append(order)
        self.orders[order_id] = order
        print(f"Añadido el {order}")
    
    # Actualiza el estado de un pedido existente
    def update_order_status(self, order_id: int, new_status: OrderStatus):
        if order_id in self.orders:
            order = self.orders[order_id]
            order.status = new_status
            print(f"Actualizado el {order}")
        else:
            print(f"Pedido con ID {order_id} no encontrado...")
    
    # Lista todos los pedidos que se encuentren en el estado especificado
    def get_orders_by_status(self, status: OrderStatus):
        orders_by_status = [order for order in self.orders.values() if order.status == status]
        return orders_by_status
    
    # Devuelve el número de pedidos por estado
    def get_num_orders_by_status(self) -> Counter:
        num_orders_by_status = Counter(order.get_status() for order in self.orders.values())
        return num_orders_by_status

# Zona de pruebas    
# 1. Instanciamos el gestor de pedidos
gestor = OrderManager()

# Añadimos 5 pedidos (por defecto en estado 'pendiente')
gestor.add_order(1)
gestor.add_order(2)
gestor.add_order(3)
gestor.add_order(4)
gestor.add_order(5)
gestor.add_order(6)

# Listamos cola de pedidos no finalizados
print("\nCola de pedidos activos:\n")
for pedido in gestor.orders_queue:
    print(f"  - {pedido}")

# Listamos el número de pedidos por estado
print("\nNúmero de pedidos actuales por estado:\n")

num_pedidos_por_estado = gestor.get_num_orders_by_status()

pedidos_pendientes = gestor.get_orders_by_status(OrderStatus.PENDING)
print(f"  - Pedidos pendientes: {len(pedidos_pendientes)}")
      
pedidos_enviados = gestor.get_orders_by_status(OrderStatus.SHIPPED)
print(f"  - Pedidos enviados: {len(pedidos_enviados)}")

pedidos_entregados = gestor.get_orders_by_status(OrderStatus.DELIVERED)
print(f"  - Pedidos entregados: {len(pedidos_entregados)}")

# Pasamos algunos pedidos al estado 'enviado'
gestor.update_order_status(1, OrderStatus.SHIPPED)
gestor.update_order_status(2, OrderStatus.SHIPPED)
gestor.update_order_status(5, OrderStatus.SHIPPED)

# Pasamos algunos pedidos al estado 'entregado'
gestor.update_order_status(3, OrderStatus.DELIVERED)
gestor.update_order_status(4, OrderStatus.DELIVERED)

# Listamos cola de pedidos no finalizados
print("\nCola de pedidos activos:\n")
for pedido in gestor.orders_queue:
    print(f"  - {pedido}")

# Listamos el número de pedidos por estado
print("\nNúmero de pedidos actuales por estado:\n")

num_pedidos_por_estado = gestor.get_num_orders_by_status()

pedidos_pendientes = gestor.get_orders_by_status(OrderStatus.PENDING)
print(f"  - Pedidos pendientes: {len(pedidos_pendientes)}")
      
pedidos_enviados = gestor.get_orders_by_status(OrderStatus.SHIPPED)
print(f"  - Pedidos enviados: {len(pedidos_enviados)}")

pedidos_entregados = gestor.get_orders_by_status(OrderStatus.DELIVERED)
print(f"  - Pedidos entregados: {len(pedidos_entregados)}")