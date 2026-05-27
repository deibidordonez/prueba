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

print(cursos)
print("="*100)
print(estudiantes)
print("="*100)
print(notas)
print("="*100)

def eliminar_estudiante(notas, estudiantes):
    print("Documentos estudiantes:", estudiantes)
    doc=int(input("\n Digite el numero del documento del estudiante que quiere eliminar: "))
    li=0
    for i in estudiantes:
        if i == doc:
            estudiantes.remove(doc)
            sup=notas[li]
            notas.remove(sup)
        li+=1
    return estudiantes,notas
estudiantes, notas=eliminar_estudiante(notas, estudiantes)
print(estudiantes, notas)

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
def promedio(notas_est):
    suma = 0
    count=0
    for n in notas_est:
        if n >= 0:
            suma += n
            count += 1
        if count == 0:
            return 0
    return suma/count
def burbble_sort(idx, promedio):
    n = len(idx)
    for i in range (n-1):
        for j in range (n-1-i):
            if promedio[idx[j]]<promedio[idx[j+1]]:
                idx[j],idx[j+1]=idx[j+1],idx[j]
def selection_sort(idx, cantidad_cursos):
    n = len(idx)
    for i in range(n - 1):
        max_pos = i
        for j in range(i + 1, n):
            if cantidad_cursos[idx[j]] > cantidad_cursos[idx[max_pos]]:
                max_pos = j
            if max_pos != i:
                idx[i], idx[max_pos] = idx[max_pos], idx[i]
prom_notas=[]
for i in range(len(notas)):
    prom_notas.append(promedio(notas(i)))
idx=[]
count=0
for i in range(len(estudiantes)):
    idx.append(count)
    count+=1
print(burbble_sort(idx, prom_notas))