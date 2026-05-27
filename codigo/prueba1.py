def cargar_datos(nombre):
    cursos = []
    estudiantes = []
    notas = []
    with open(nombre, 'r') as f:
        lineas = f.readlines()
    # Línea 0: códigos de cursos
    cursos = lineas[0].strip().split(',')
    # Línea 1: documentos estudiantes
    for doc in lineas[1].strip().split(','):
        estudiantes.append(int(doc))
    # Líneas 2..n: notas por estudiante
    for linea in lineas[2:]:
        fila = []
        for val in linea.strip().split(','):
            fila.append(float(val))
        notas.append(fila)
    return cursos, estudiantes, notas
cursos, estudiantes, notas=cargar_datos("notas_estudiantes.csv")
"""
print(cursos)
print("="*100)
print(estudiantes)
print("="*100)
print(notas)
print("="*100)
"""
def eliminar_estudiante(notas, estudiantes):
    print("Documentos estudiantes:", estudiantes)
    doc=int(input("\n Digite el numero del documento del estudiante que quiere eliminar: "))
    l=0
    for i in estudiantes:
        if i == doc:
            estudiantes.remove(doc)
            sup=notas[l]
            notas.remove(sup)
        l+=1
    return estudiantes,notas
#estudiantes, notas=eliminar_estudiante(notas, estudiantes)
#print(estudiantes, notas)

def buscar(doc, estudiantes):
    for i in range(len(estudiantes)):
        if estudiantes[i] == doc:
            return i
    if doc == estudiantes[-1]:
        return -1
    return None

def mayor_nota(doc, estudiantes, cursos, notas):
    i = buscar(doc, estudiantes) # Búsqueda lineal
    max_n = -99
    max_c = ""
    for j in range(len(cursos)):
        n = notas[i][j]
        if n >= 0 and n > max_n: # Ignora -1 y -2
            max_n = n
            max_c = cursos[j]
    return max_n, max_c
m = mayor_nota(1024351175, estudiantes, cursos, notas)
print("mayor nota: ", m)