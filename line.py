import math
def line():
    a = float(input("Ingrese el coeficiente A:"))
    b = float(input("Ingrese el coeficiente B:"))
    x1 = float(input("Ingrese el coeficiente X1:"))
    x2 = float(input("Ingrese el coeficiente X2:"))
    y1 = float(a * x1 + b)
    y2 = float(a * x2 + b) 
    p1 = [x1 , y1]
    p2 = [x2 , y2]
    distance = float(math.dist(p1,p2))
    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x2}")
    print("\n2")
    print("Para la siguient ecuación:")
    print(f"\t Y = {a}X + {b}")
    print("\n") 
    print("Dados los siguientes puntos:")
    print(f"\t P1 ({x1} ; {y1})")
    print(f"\t P2 ({x2} ; {y2})")
    print("\n")
    print(f"La distancia entre ellos es: {distance}")
