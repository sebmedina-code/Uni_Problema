grades = {'Alice': 20, 'Bob': 18, 'Charlie': 5, 'Dennis': 10, 'Eve': 13, 'Frank': 13, 'Gaby': 14, 'Hugh': 3, 'Isaac': 9}

estudiante_min = None
nota_min = int('inf')

for estudiante, nota in grades.items():
    if nota < nota_min:
        nota_min = nota
        estudiante_min = estudiante

print(f"El estudiante con la nota más baja es {estudiante_min} con un {nota_min}.")