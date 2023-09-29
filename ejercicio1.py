class Articulo:
    def __init__(self, nombre, cantidad, precio):
        # Inicializar los atributos del artículo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            # Verificar si hay suficiente cantidad en stoc para la venta
            self.cantidad -= cantidad_vendida
            total_venta = cantidad_vendida * self.precio
            return f"Venta realizada. Total a pagar: ${total_venta}"
        else:
            return "No hay suficiente stoc para realizar la venta."

# Ejemplo de uso
producto1 = Articulo("Camiseta", 50, 20.99)
print(producto1.vender(10))  # Realizar una venta de 10 unidades
