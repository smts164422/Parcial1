class Producto:
    def __init__(self, nombre, cantidad, precio_compra, precio_venta):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

    def vender(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            return self.precio_venta * cantidad
        else:
            print("Cantidad insuficiente en inventario.")
            return 0

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad, precio_compra, precio_venta):
        if nombre in self.productos:
            self.productos[nombre].actualizar_cantidad(cantidad)
        else:
            nuevo_producto = Producto(nombre, cantidad, precio_compra, precio_venta)
            self.productos[nombre] = nuevo_producto

    def registrar_venta(self, nombre, cantidad, pago_cliente):
        if nombre in self.productos:
            total_venta = self.productos[nombre].vender(cantidad)
            if total_venta > 0:
                if pago_cliente >= total_venta:
                    vuelto = pago_cliente - total_venta
                    print(f"Venta registrada. Total: ${total_venta:.2f}. Vuelto: ${vuelto:.2f}")
                else:
                    print("El monto pagado es insuficiente para realizar la compra.")
                    self.productos[nombre].actualizar_cantidad(cantidad)  # Devolver el producto al inventario
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        print("\nInventario actual:")
        for producto in self.productos.values():
            print(f"{producto.nombre}: {producto.cantidad} unidades a ${producto.precio_venta:.2f} cada una")

def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar producto")
        print("2. Registrar venta")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio_compra = float(input("Ingrese el precio de compra: "))
            precio_venta_sugerido = float(input("Ingrese el precio de venta sugerido: "))
            inventario.agregar_producto(nombre, cantidad, precio_compra, precio_venta_sugerido)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto vendido: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            pago_cliente = float(input("Ingrese el monto pagado por el cliente: "))
            inventario.registrar_venta(nombre, cantidad, pago_cliente)
        elif opcion == '3':
            inventario.mostrar_inventario()
        elif opcion == '4':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()