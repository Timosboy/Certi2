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
    a = float(input("lado A: "))
    b = float(input("lado B: "))
    c = float(input("lado C: "))

    if not triangulovalido(a, b, c):
        print("No tiene la forma de un triangulo.")
    else:
        tipo = tipotriangulo(a, b, c)
        print(f"El triangulo es {tipo}")


if __name__ == "__main__":
    main()