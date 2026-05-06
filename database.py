# --- FUNCIONES DE APOYO ---

def limpiar_linea(cadena):
    """
    Elimina espacios y saltos de línea al inicio y final
    """
    inicio = 0
    while inicio < len(cadena) and (cadena[inicio] == ' ' or cadena[inicio] == '\n' or cadena[inicio] == '\r'):
        inicio += 1
    fin = len(cadena) - 1
    while fin >= 0 and (cadena[fin] == ' ' or cadena[fin] == '\n' or cadena[fin] == '\r'):
        fin -= 1
    return cadena[inicio:fin+1]

def separar_texto(cadena, separador):
    """
    Divide una cadena por un separador dado
    """
    resultado = []
    actual = ""
    for char in cadena:
        if char == separador:
            resultado.append(actual)
            actual = ""
        else:
            actual += char
    resultado.append(actual)
    return resultado

def inicia_con(cadena, prefijo):
    """
    Verifica si la cadena comienza con un caracter
    """
    if len(cadena) < len(prefijo):
        return False
    return cadena[:len(prefijo)] == prefijo

# --- FUNCIONES DE CARGA Y GUARDADO ---

def cargar_usuarios():
    """
    Carga credenciales desde users.txt.
    """
    cred = {}
    try:
        with open("users.txt", "r", encoding="utf-8") as f:
            for linea in f:
                limpia = limpiar_linea(linea)
                if limpia != "":
                    datos = separar_texto(limpia, ";")
                    cred[datos[0]] = datos[1]
    except FileNotFoundError:
        print("Archivo users.txt no encontrado.")
    return cred

def cargar_datos_red():
    """
    Construye la red social desde userData.txt.
    """
    red = {}
    u_actual = ""
    try:
        with open("userData.txt", "r", encoding="utf-8") as f:
            for linea in f:
                limpia = limpiar_linea(linea)
                if inicia_con(limpia, "*"):
                    # Procesar *nombre:amigos,<solicitudes>
                    contenido = limpia[1:]
                    partes = separar_texto(contenido, ":")
                    u_actual = partes[0]
                    resto = partes[1]
                    
                    amigos_raw = ""
                    sols_raw = ""
                    en_sols = False
                    for c in resto:
                        if c == "<": en_sols = True
                        elif c == ">": en_sols = False
                        elif en_sols: sols_raw += c
                        else: amigos_raw += c
                    
                    red[u_actual] = {
                        "amigos": [a for a in separar_texto(amigos_raw, ",") if a != ""],
                        "solicitudes": [s for s in separar_texto(sols_raw, ";") if s != ""],
                        "intereses": [],
                        "mensajes": []
                    }
                elif inicia_con(limpia, "{"):
                    red[u_actual]["intereses"] = separar_texto(limpia[1:-1], ",")
                elif limpia != "":
                    red[u_actual]["mensajes"].append(limpia)
    except FileNotFoundError:
        print("Archivo userData.txt no encontrado.")
    return red

def guardar_todo(cred, red):
    """
    Persistencia total en archivos de texto.
    """
    # Guardar users.txt
    with open("users.txt", "w", encoding="utf-8") as f:
        for u, c in cred.items():
            f.write(u + ";" + c + "\n")
            
    # Guardar userData.txt
    with open("userData.txt", "w", encoding="utf-8") as f:
        for u, d in red.items():
            amigos = ""
            for i in range(len(d["amigos"])):
                amigos += d["amigos"][i] + ("," if i < len(d["amigos"])-1 else "")
            
            sols = ""
            for i in range(len(d["solicitudes"])):
                sols += d["solicitudes"][i] + (";" if i < len(d["solicitudes"])-1 else "")
            
            cabecera = "*" + u + ":" + amigos
            if sols != "": cabecera += ",<" + sols + ">"
            f.write(cabecera + "\n")
            
            if d["intereses"]:
                ints = "{"
                for i in range(len(d["intereses"])):
                    ints += d["intereses"][i] + ("," if i < len(d["intereses"])-1 else "")
                f.write(ints + "}\n")
                
            for m in d["mensajes"]:
                f.write(m + "\n")
            f.write("\n")