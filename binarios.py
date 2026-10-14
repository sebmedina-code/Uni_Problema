
num1 = int(input("ingrese un numero: "))
print(bin(num1))
s1 = bin(num1)
print(s1)
num2 = int(input("ingrese segundo numero: "))
print(bin(num2))
s2 = bin(num2)
l = 5

for i in range(2, 5):
    print(s1[i])
    print(s2[l])
    l = l - 1