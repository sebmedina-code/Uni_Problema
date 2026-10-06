n = []

while True:
    numero = int(input("ingrese un numero positivo y entero: "))
    if numero >= 0:
        n.append(numero)
    else:
        break
n.sort()
n.reverse()
print("los numeros ingresados son:", n)
print("Sigue haciendolo ")


while True:
    numero = int(input("ingrese un numero positivo y entero: "))
    if numero >= 0:
        n.append(numero)
    else:
        break
n.sort()
n.reverse()
print("los numeros ingresados son:", n)
print("terminado")
