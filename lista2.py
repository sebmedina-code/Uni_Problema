numero = int(input("ingrese un número entre positivo: "))
suma = 0
i = 1

while i < numero:
    if numero % i == 0:
        print(f"{i} es divisor de {numero}")
        suma += i
    i += 1
if suma == numero:
    print(f"{numero} es un número perfecto")
else:
    print(f"{numero} no es un número perfecto")