def plus_one(num):
    print(num + 2)
result = plus_one(2)
print(type(result))





def plus_one(num):
    return num + 1
result = plus_one(1)
print(result)
print(type(result))




def simple_func(msg):
    msg = 'mensaje'
    print(msg)
print(simple_func('hola'))




contador = 0
def sumador(contador):
    contador += 12
    return contador
print(sumador(contador))
print(contador)





greet(['Juan', 'Pedro', 'Maria', 'Lucas'])
def greet(name):
    for name in name:
        print(f"Hola {name}")




def square_area(side=1):
    return side**2
def area(calculation, **params):
    if params["type"] == "square":
        return calculation(params["side"])
    return None
print(area(square_area, side=2, type="square", other=1))



def imprimir_diccionario(**diccionarios):
    print("Diccionario:")
    for clave, valor in diccionarios.items():
        print(f"{clave}: {valor}")
imprimir_diccionario(nombre="Juan", edad=25, ciudad="Madrid", ocupacion="Ingeniero")
imprimir_diccionario(producto="Laptop", precio="1200", stock=5)



def volumen_cilindro(radio, altura):
    pi = 3.14159
    resultado = pi * (radio ** 2) * altura
    return resultado
print(volumen_cilindro(3, 5))  # Ejemplo de uso