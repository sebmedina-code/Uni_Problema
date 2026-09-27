#problema N*3

num_list = []

contador_impares = 0
suma_impares = 0
indice = 0
size = len(num_list)
while (contador_impares < 5) and (indice < size):
    if num_list[indice] % 2 != 0:
        contador_impares += 1
        suma_impares += num_list[indice]
    indice += 1
print(f"hay {contador_impares} numeros impares")
print(f"La suma es {suma_impares} de numeros impares")