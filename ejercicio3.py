class Habitacion:
    def __init__(self, tipo, precio_por_noche):
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche

class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.habitacion = None
        self.noches = 0
        self.servicios_extra = []

    def elegir_habitacion(self, habitacion, noches):
        self.habitacion = habitacion
        self.noches = noches

    def agregar_servicio_extra(self, servicio):
        self.servicios_extra.append(servicio)

    def calcular_total(self):
        total = self.habitacion.precio_por_noche * self.noches
        for servicio in self.servicios_extra:
            total += servicio.precio
        return total

class ServicioExtra:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente

    def generar_factura(self):
        total = self.cliente.calcular_total()
        print(f"\nFactura para {self.cliente.nombre}")
        print(f"Habitación: {self.cliente.habitacion.tipo}")
        print(f"Número de noches: {self.cliente.noches}")
        print("Servicios extra:")
        for servicio in self.cliente.servicios_extra:
            print(f" - {servicio.nombre}: ${servicio.precio:.2f}")
        print(f"Total: ${total:.2f}\n")

def main():
    # Crear algunas habitaciones y servicios
    habitacion_simple = Habitacion("Simple", 50)
    habitacion_lujo = Habitacion("Lujo", 120)
    piscina = ServicioExtra("Uso de la piscina", 10)
    golf = ServicioExtra("Uso de la cancha de golf", 20)

    # Registrar un cliente
    cliente = Cliente("Juan Pérez", "12345678")
    cliente.elegir_habitacion(habitacion_lujo, 3)

    # Agregar servicios extra
    cliente.agregar_servicio_extra(piscina)
    cliente.agregar_servicio_extra(golf)

    # Generar factura
    factura = Factura(cliente)
    factura.generar_factura()

if __name__ == "__main__":
    main()