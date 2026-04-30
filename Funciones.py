
def cargar_usuarios(archivo):
    """
    Esta funcion abre un archivo de texto en el cual
    se encuentran todos los usuarios y contraseñas del
    programa a realizar. Esta funcion retorna un diccionario
    en cual divide los usuarios y contraseñas
    """
    dic_credenciales = {}
    for line in archivo:
        if ";" in line:
            posicion_separador = line.index(";")
            usuario = line[: posicion_separador]
            contrasena_con_salto = line[posicion_separador + 1:]
            if contrasena_con_salto[-1] == '\n':
                contrasena = contrasena_con_salto[:-1]
            else:
                contrasena = contrasena_con_salto
            dic_credenciales [usuario] = contrasena
    return dic_credenciales

def guardar_usuarios(usu):
    """
    Esta funcion sirve para registrar y almacenar nuevos usuarios en la red social
    que se realiza en este codigo.
    """
    a = True
    while a == True:
        b=False
        new_user= input("Registre un nuevo usuario: ")
        new_contra= input("Registre la contraseña del usuario: ")
        for i in usu:
            if i == new_user:
                print("El usuario ya esta registrado")
                b = True
        if b == True:
            continue
        else:
            usu[new_user] = new_contra
            a =False     
    return usu



def cargar_datos_red(usu_a):
    """
    Esta funcion revisa un archivo tipo txt y genera un diccionario de la siguiente manera:
    dic_info = {"carlos":{ 
                           "amigos": ["jose","sebastian"],
                           "solicitudes":[],
                           "gustos":[],
                           "mensajes":[ # MENSAJES RECIBIDOS
                           "El 23/09/2018 14:37:26 jose escribió: Me alegro mucho, y como va el trabajo?",
                           "El 23/09/2018 14:35:01 jose escribió: Hola Carlos, como estás?"]}},
                 "jose":{
                           "amigos": ["carlos","sebastian"],
                           "gustos":[],
                           "mensajes": [# MENSAJES RECIBIDOS
                           ""],}}
    en el cual se cuentra la informacion de todos y cada uno de los usuarios
    """
    dic_info = {}
    for i in usu_a :
        if not i in dic_info:
            new_info ={i:{"amigos":[],"solicitudes":[], "gustos":[], "mensajes":[]}}

    pass

def guardar_datos_red():
    """
    
    """
    pass


        
    


