class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido




class Cliente(Persona):
    def __init__(self, nombre, apellido, cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nCuenta: {self.cuenta}\nBalance de cuenta: ${self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Depósito de ${cantidad} realizado con éxito. Nuevo balance: ${self.balance}")

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= cantidad
            print(f"Retiro de ${cantidad} realizado con éxito. Nuevo balance: ${self.balance}")

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    cuenta = input("Ingrese el número de cuenta del cliente: ")
    balance = float(input("Ingrese el balance inicial de la cuenta: "))
    return Cliente(nombre, apellido, cuenta, balance)

def Inicio():
    print("Bienvenido al sistema de cuentas bancarias")
    cliente = crear_cliente()
    print(cliente)
    opc = 0

    while opc != 3:
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opc = int(input("Seleccione una opción: "))
        if opc == 1:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opc == 2:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opc == 3:
            print("Gracias por usar el sistema de cuentas bancarias")
        else:
            print("Opción inválida")

Inicio()
