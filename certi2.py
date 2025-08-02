import math
from fractions import Fraction

def pedir_lado(nombre):
    while True:
        valor = input(f"Lado {nombre} (o 'q' para salir): ").strip()
        if valor.lower() in ['q', 'salir']:
            print("Bye Bye.")
            exit()

        if not valor:
            print("Error: No puedes dejar el valor vacío.")
            continue

        valor = valor.replace(',', '.')

        try:
            if '/' in valor:
                lado = float(Fraction(valor))
            else:
                lado = float(valor)
        except ValueError:
            print("Error: Debes ingresar un número o una fracción (ejemplo: 3/4).")
            continue

        if lado <= 0:
            print("Error: El lado debe ser un número positivo mayor que cero.")
            continue

        if math.isnan(lado) or math.isinf(lado):
            print("Error: Número inválido, no uses NaN o infinito).")
            continue

        return lado

def tipotriangulo(a, b, c):
    if a == b == c:
        return "EQUILATERO"
    elif a == b or b == c or a == c:
        return "ISOSCELES"
    else:
        return "ESCALENO"

def triangulovalido(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def main():
    try:
        a = pedir_lado("A")
        b = pedir_lado("B")
        c = pedir_lado("C")

        if not triangulovalido(a, b, c):
            print("No tiene la forma de un triángulo.")
        else:
            tipo = tipotriangulo(a, b, c)
            print(f"El triángulo es {tipo}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main()
