notas = [14, 8, 19, 3, 16, 11, 20, 7, 15, 9, 18, 5, 12, 6, 17, 10, 13, 4, 8.5, 19.5, 2, 15.5, 9.5, 14.5, 11.5, 1, 16.5, 7.5, 12.5, 6.5, 17.5, 10.5, 13.5, 4.5, 18.5]
print ("notas originales: ", notas)
notas.sort(reverse=True)
#notas.sort()
#notas [::-1]
print("notas ordenadas de mayor a menor", notas)

notas10 = []
ctd_notas10 = 0
ctd_notas9 = 0
notas_menor9 = []
for nota in notas:
    if nota >= 9.5:
        notas10.append(nota)
        ctd_notas10 += 1
    else:
        notas_menor9.append(nota)

print("aprobados", notas10)
print("desaprobados:", notas_menor9)
print("cantidad de notas >= 9.5:", len(notas10))
print("cantidad de notas >= 9.5:", ctd_notas10)

contador_notas10 = len(notas10)
contador_notas_menor9 = len(notas_menor9)

promedio_notas10 = sum(notas10) / contador_notas10
promedio = sum(notas) / len(notas)
promedio_notas_menor9 = sum(notas_menor9) / contador_notas_menor9

print(f"Promedio general: {promedio}")
print(f"Promedio aprobados: {promedio_notas10}")
print(f"Promedio desaprobados: {promedio_notas_menor9}")
