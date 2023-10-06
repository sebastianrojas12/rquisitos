# math para poder usar funciones matemáticas
import math

# Función para sumar dos números
def sumar(n1, n2):
  return n1 + n2

# Función para restar dos números
def restar(n1, n2):
  return n1 - n2

# Función para multiplicar dos números
def multiplicar(n1, n2):
  return n1 * n2

# Función para dividir dos números
def dividir(n1, n2):
  return n1 / n2


# Función principal
def main():
  # Solicitamos al usuario los dos números a operar
  n1 = float(input("Introduce el primer número: "))
  n2 = float(input("Introduce el segundo número: "))

  # Imprimimos el menú de opciones
  print("Elige una operación:")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")

  # Solicitamos al usuario la operación que desea realizar
  opcion = int(input("Introduce la opción: "))

  # Realizamos la operación seleccionada
  if opcion == 1:
    print("La suma de los números es:", sumar(n1, n2))
  elif opcion == 2:
    print("La resta de los números es:", restar(n1, n2))
  elif opcion == 3:
    print("La multiplicación de los números es:", multiplicar(n1, n2))
  elif opcion == 4:
    print("La división de los números es:", dividir(n1, n2))
 

# Llamamos a la función principal
if __name__ == "__main__":
  main()