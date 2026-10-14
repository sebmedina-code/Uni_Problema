secciones = [ ['maria','andres','pedro'], ['stefania','gabriel','julia','manuel']]

for sec in range(len(secciones)):
    for estudiante in range(len(secciones[sec])):
        print("el estudiante {} está en la seccion {}".format(secciones[sec][estudiante], sec+1))