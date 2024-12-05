import datetime

"""
Clase que contiene el identificador, el saldo y
el registro de transacciones de una cuenta bancaria
"""
class CuentaBancaria:
    def __init__(self, id: int, saldo: float = 0.00):
        self.id = id
        self.saldo = saldo
        self.registro = [
            # {
            #     'id': 1,
            #     'saldo_anterior': 0.00,
            #     'tipo_transacción': TransactionType.INCOME,
            #     'fecha': datetime.datetime.now(),
            #     'importe': 2100.00,
            #     'nuevo_saldo': 2100.00
            # },
            # {
            #     'id': 2,
            #     'saldo_anterior': 2100.00,
            #     'tipo_transacción': TransactionType.EXPENSE,
            #     'fecha': datetime.datetime.now(),
            #     'importe': 15.50,
            #     'nuevo_saldo': 2084.50
            # },
            # {
            #     'id': 3,
            #     'saldo_anterior': 2084.50,
            #     'tipo_transacción': TransactionType.EXPENSE,
            #     'fecha': datetime.datetime.now(),
            #     'importe': 33.75,
            #     'nuevo_saldo': 2050.75
            # },
            # {
            #     'id': 4,
            #     'saldo_anterior': 2025.75,
            #     'tipo_transacción': TransactionType.INCOME,
            #     'fecha': datetime.datetime.now(),
            #     'importe': 200.00,
            #     'nuevo_saldo': 2250.75
            # },
        ]
    
    def mostrar_transacciones(self):
        print("\n\n=======================================================================================")
        print(f"REGISTRO DE TRANSACCIONES [CUENTA {self.id}]")
        print("---------------------------------------------------------------------------------------")
        print("#TRANSACCIÓN\tSALDO_ANTERIOR\tTIPO_TRANSACCIÓN\tIMPORTE\t\tNUEVO_SALDO")
        print("=======================================================================================\n")

        transaction_type = 0

        for transaccion in self.registro:
            if transaccion['tipo_transacción'] == 2:
                transaction_type = 'GASTO'
            else:
                transaction_type = 'INGRESO'

            print(f"{transaccion['id']}\t\t{transaccion['saldo_anterior']}\t\t{transaction_type}\t\t\t{transaccion['importe']}\t\t{transaccion['nuevo_saldo']}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    
    # Calcula el ID de una nueva rtransacción (si no hay transacciones registradas, será 1)
    def _new_transaction_id(self) -> int:
        # Calculamos el ID de la nueva transacción (si no hay transacciones, será 1)
        if len(self.registro) == 0:
            return 1
        else:
            new_id = max(self.registro, key=lambda transaccion: transaccion['id'])['id'] + 1
            return new_id
    
    # Método protegido. Se avisa por convencion de que no debe ser usado
    # fuera de la clase, aunque puede serlo
    def _actualizar_saldo(self, tipo_transaccion: int, importe: float):
        saldo_anterior = self.saldo
        fecha_transaccion = datetime.datetime.now()

        if tipo_transaccion == 2:
            self.saldo -= importe  # Gasto
        else:
            # print("Transacción de tipo INGRESO")
            self.saldo += importe  # Ingreso
        
        self.__registrar_transaccion(saldo_anterior, tipo_transaccion, importe, self.saldo)
        
    
    # Método privado. Solo puedes ser usado dentro de la clase
    def __registrar_transaccion(self, saldo_anterior, tipo_transaccion: int, importe: float, nuevo_saldo: float):    
        transaccion = {
            'id': self._new_transaction_id(),
            'saldo_anterior': saldo_anterior,
            'tipo_transacción': tipo_transaccion,
            'fecha': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'importe': importe,
            'nuevo_saldo': nuevo_saldo
        }
        self.registro.append(transaccion)
        print(f"\nSe ha registrado la siguiente transacción:\n\t{transaccion}")

cuenta_bancaria_1 = CuentaBancaria(18201540679321456789)

cuenta_bancaria_1.mostrar_transacciones()

cuenta_bancaria_1._actualizar_saldo(1, 2100.00)    # 1 = INGRESO
cuenta_bancaria_1._actualizar_saldo(2, 15.50)      # 2 = GASTO
cuenta_bancaria_1._actualizar_saldo(2, 33.75)      # 2 = GASTO
cuenta_bancaria_1._actualizar_saldo(1, 200.00)     # 1 = INGRESO

cuenta_bancaria_1.mostrar_transacciones()