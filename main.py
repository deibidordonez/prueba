import database as db
import datetime

def validar_opcion(min_val, max_val):
    """
    validacion de rango de opciones de menu_seion e inicio
    """
    while True:
        try:
            opc = int(input(f"Seleccione ({min_val}-{max_val}): "))
            if min_val <= opc <= max_val: return opc
            print("Fuera de rango.")
        except ValueError:
            print("Error: Ingrese solo números.")

def menu_sesion(usuario, cred, red):
    """
    Funcion del menu principal al iniciar la seccion
    """
    while True:
        print(f"\n--- PERFIL DE {usuario} ---")
        print(f"Amigos: {len(red[usuario]['amigos'])} | Solicitudes: {len(red[usuario]['solicitudes'])}")
        print("1. Ver usuarios")
        print("2. Enviar solicitud")
        print("3. Ver solicitudes y aceptar")
        print("4. Ver mensajes")
        print("5. Enviar mensaje")
        print("6. Ver amigos")
        print("7. Añadir intereses")
        print("8. Cerrar sesión")
        
        opc = validar_opcion(1, 8)
        #%% modulo de opciones del menu del usuario
        if opc == 1:
            for u in red: print("-", u)
        elif opc == 2:
            destino = input("Destinatario: ")
            if destino not in red:
                print(f"El usuario {destino} no existe.")
            elif destino == usuario: 
                print("No puedes enviarte a ti mismo.")
            elif destino in red[usuario]["amigos"]: 
                print("Ya son amigos.")
            elif usuario in red[destino]["solicitudes"]: 
                print("Ya enviada.")
            else:
                red[destino]["solicitudes"].append(usuario)
                print("Solicitud enviada.")
        elif opc==3:
            print("\n Tienes solicitudes de:")
            con=1
            c=False
            for i in red[usuario]["solicitudes"]:
                c=True
                print(f"{con}. {i}")
                con= con + 1
            if c == True:
                acep=input("¿Desea aceptar alguna solicitud? (Si/No) : ")
                if acep == "si" or acep == "SI" or acep == "sI" or acep == "Si":
                    a = True
                    while a == True:
                        acep=input("Ingrese el nombre del usuario: ")
                        for i in acep:
                            if i in ("1","2","3","4","5","6","7","8","9","0"):
                                print("Ingrese solo nombres")
                                break
                            else:
                                if acep in red[usuario]["solicitudes"]:
                                    red[usuario]["solicitudes"].remove(acep)
                                    red[usuario]["amigos"].append(acep)
                                    red[acep]["amigos"].append(usuario)
                                    print("Amigo agregado")
                                    a = False
                                    break
                                else:
                                    print("No tiene una solicitud del usuario ingresado")
                                    break
                elif acep == "no" or acep == "No" or acep == "nO" or acep == "NO":
                    acep=input("¿Desea eliminar las solicitudes?: ")
                    if acep == "si" or acep == "Si" or acep == "sI" or acep == "SI":
                        for i in red[usuario]["solicitudes"]:
                                red[usuario]["solicitudes"].remove(i)
            else:
                print("No tienes solicitudes de amistad")
                
        elif opc == 4:
            for m in red[usuario]["mensajes"]: print(m)
        elif opc == 5:
            destinatario=input("¿A quien desea enviarle el mensaje?: ")
            fecha_formateada = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            mns = f"El {fecha_formateada} {usuario} escribio: "
            mns+=(input("Ingrese mensaje a enviar: "))
            if destinatario not in red:
                print("El usuario a enviar el mensaje no existe")
            elif destinatario == usuario:
                print("No te puedes enviar mensajes a ti mismo")
            elif destinatario not in red[usuario]["amigos"]:
                print("No puedes enviarles mensajes a personas que no estan entre tus amigos")
            else:
                red[destinatario]["mensajes"].append(mns)
                print("Mensaje enviado correctamente")
        
        elif opc==6:
            n=1
            print(f"\n Amigos de {usuario}:")
            for i in red[usuario]["amigos"]:
                print(n , i)
                n+=1

        elif opc == 7:
            ax = "si"
            while ax=="si" or ax=="Si" or ax=="sI" or ax=="SI":
                interes=input("ingrese sus intereses: ")
                red[usuario]["intereses"].append(interes)
                ax=input("¿Desea ingresar mas interese? (si/no): ")

        elif opc == 8:
            break
        db.guardar_todo(cred, red)
        #%%<Fin>
def inicio():
    """
    Funcio que carga toda la red social
    """
    credenciales = db.cargar_usuarios()
    red = db.cargar_datos_red()
    
    while True:
        print("\n--- RED SOCIAL UDEA ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        
        opc = validar_opcion(1, 3)
        #%% Modulo de opciones del menu inicio
        if opc == 1:
            nom = input("Nuevo usuario: ")
            if nom in credenciales: print("Ya existe.")
            else:
                clave = input("Contraseña: ")
                credenciales[nom] = clave
                red[nom] = {"amigos":[], "solicitudes":[], "intereses":[], "mensajes":[]}
                db.guardar_todo(credenciales, red)
                print("Registro exitoso.")
        elif opc == 2:
            u = input("Usuario: ")
            c = input("Clave: ")
            if u in credenciales and credenciales[u] == c:
                menu_sesion(u, credenciales, red)
            else:
                print("Credenciales incorrectas.")
        else:
            break
        #%% <Fin>
if __name__ == "__main__":
    inicio()