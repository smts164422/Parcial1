"""
    Programa que permita imprimirla boleta de pago de 
    trabajadores segun sean de plaza fija o por horas
    variables:
                -PagoxHora = $4
                -Comisiones = %15
                -Bono 5 años = %10
"""
plazaFija = []
plazaXHora = []

r = True
var = input("Ingresar Trabajadores? S/N: ")
if var == "S":
    plaza = input("Tipo de plaza? Fija= 1 || xHora= 2: ")
    while r:
        if plaza == "1":
            Nombre = input("Dijite el nombre: ")
            plazaFija.append(Nombre)
            Sueldo = float(input("Sueldo: "))
            plazaFija.append(Sueldo)
            añosTrabajo = int(input("Tiempo de trabajo en años: "))
            plazaFija.append(añosTrabajo)
        elif plaza == "2":
            Nombre = input("Ingrese el nombre: ")
            plazaXHora.append(Nombre)
        var2 = input("Ingresar otro nombre? S/N: ")
        if var2 != "S":
            r = False

for i in plazaFija:
    print(f"Nombre: {i}")
else:
    print("\nFin del programa")