suma = 0
while True:
    n = int(input("Ingrese numero positivo entero: "))
    if n>=0:
        suma+n
    else:
        break
print(f"la suma de los numeros es: {suma}")