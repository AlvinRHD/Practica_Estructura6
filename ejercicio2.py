class Usuario:
    def __init__(self, nombre, correo, saldo_inicial):
        # Inicializar los atributos del usuario
        self.nombre = nombre
        self.correo = correo
        self.saldo = saldo_inicial

    def depositar(self, monto):
        # Realizar un depósito en la cuenta del usuario
        self.saldo += monto
        return f"Se ha depositado ${monto}. Saldo actual: ${self.saldo}"

    def retirar(self, monto):
        if monto <= self.saldo:
            # Verificar si hay suficiente saldo para el retiro
            self.saldo -= monto
            return f"Se ha retirado ${monto}. Saldo actual: ${self.saldo}"
        else:
            return "Saldo insuficiente para realizar el retiro."

# Ejemplo de uso
usuario1 = Usuario("Alvin Rosales", "alvin@ejemplo.com", 1000)
print(usuario1.depositar(500))  # Realizar un depósito de $500
print(usuario1.retirar(300))    # Realizar un retiro de $300
