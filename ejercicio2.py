"""
    Prorama que registre la asistencia
"""
#Creacion de la clase Asistencia()
class Asistencia:
    #Implementacion de los parámetros de la clase
    Nombre = "None"
    Edad = 0
    Grado = "None"
    Asistió = "None"
    Permiso = "None"

#Creacion de una función que le dará el valor al parámetro Asistió
def Falt(asis):
    if asis == "S":
        presencia = "Si"
    elif asis == "N":
        presencia == "No"
    return presencia

def Permi(per):
    if per == "S":
        respuesta = "Alumno tiene permiso"
    elif per == "N":
        respuesta = "Alumno no tiene permiso"
    return respuesta

#Función que mandará los datos ingresados a su respectivo parámetro
def DatosAsistencia(Asistencia, nombre, edad, grado, asistió, ):
    Asistencia.Nombre = nombre
    Asistencia.Edad = edad
    Asistencia.Grado = grado
    Asistencia.Asistió = asistió

#Función que permitirá ingresar datos
def IngresarAsistencia(Asistencia):
    nombre = input("Ingrese nombre del estudiante: ")
    edad = input("Ingrese edad del estudiante: ")
    grado = input("Ingrese grado perteneciente: ")
    asiste = input("El estudiante asistió? S/N: ")
    asistió = Falt(asiste)
    DatosAsistencia(Asistencia, nombre, edad, grado, asistió, )

#Función que permitirá mostrar los datos al momento de instanciar el objeto
def Mostrar(Asistencia):
    print(f"\nEstudiante: {Asistencia.Nombre}"+
          f"\nEdad: {Asistencia.Edad}"+
          f"\nGrado: {Asistencia.Grado}"+
          f"\nAsistió: {Asistencia.Asistió}"+
          f"\nPermiso: {Asistencia.Permiso}")
    
#Objeto instanciado(profe1)
profe1 = Asistencia()
#Momento de ingresar los datos
IngresarAsistencia(profe1)
print("**********")
#Impresión de los datos
Mostrar(profe1)

print("\nFin del programa")
