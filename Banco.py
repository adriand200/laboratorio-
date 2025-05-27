# Clase que representa una cuenta bancaria
class CuentaBancaria: # Definición de la clase
    def __init__(self, titular, saldo_inicial=0): 
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto): # Método para depositar dinero en la cuenta
        """Deposita un monto en la cuenta del titular."""
        if monto > 0:
            self.saldo += monto
            print(f"{self.titular} depositó ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):# Método para retirar dinero de la cuenta
        """Retira un monto de la cuenta del titular."""
        if monto > self.saldo:
            print(f"{self.titular} no tiene saldo suficiente para retirar ${monto}. Saldo actual: ${self.saldo}")
        elif monto > 0:
            self.saldo -= monto
            print(f"{self.titular} retiró ${monto}. Saldo restante: ${self.saldo}")
        else:
            print("El monto a retirar debe ser mayor a 0.")

    def consultar_saldo(self):
        print(f"{self.titular} tiene un saldo de: ${self.saldo}")

# Función para simular la cola de clientes
def procesar_clientes(fila_clientes):
    while fila_clientes: # Mientras haya clientes en la fila
        cliente = fila_clientes.pop(0)  # El primero en la fila
        print(f"\nAtendiendo a {cliente.titular}")
        cliente.depositar(100)
        cliente.retirar(50)
        cliente.consultar_saldo()

# Simulación
cliente1 = CuentaBancaria("Ana", 200)
cliente2 = CuentaBancaria("Brayan", 150)
cliente3 = CuentaBancaria("Carlos", 300)

fila = [cliente1, cliente2, cliente3]
procesar_clientes(fila)