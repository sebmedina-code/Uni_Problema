#Cuenta la cantidad de frutas en su cesta. Para hacer esto, tiene el diccionario y la lista de frutas. Use el diccionario y la lista para contar el número total de frutas y los otros artículos que no son frutas en su cesta.
# Variables Globales
# OUTPUT: Hay 23 frutas en la cesta. y 13 objetos que no son frutas.
cantidad_frutas, cantidad_no_frutas = 0, 0
cesta = {'manzanas': 4, 'naranjas': 19, 'hamburgesas': 5, 'sandwiches': 8}
frutas = ['manzanas', 'naranjas', 'peras', 'parchitas', 'uvas', 'cambures']

for item in cesta:
    if item in frutas:
        cantidad_frutas += cesta[item]
    else:
        cantidad_no_frutas += cesta[item]

print(f"Hay {cantidad_frutas} frutas en la cesta.")
print(f"Hay {cantidad_no_frutas} objetos que no son frutas en la cesta.")