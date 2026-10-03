lista = [1,3,5,6,18]
suma = 0
for numero in lista:
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
        print(f"la suma de los divisores de {numero} es {suma}")
    if numero == suma:
        print(f"{numero} es un número perfecto")
    else:
        print(f"{numero} no es un número perfecto")