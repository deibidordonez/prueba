import database as db
import datetime

def validar_opcion(min_val, max_val):
    """Validación de rango y tipo de dato mediante excepciones."""
    while True:
        try:
            opc = int(input(f"Seleccione ({min_val}-{max_val}): "))
            if min_val <= opc <= max_val: return opc
            print("Fuera de rango.")
        except ValueError:
            print("Error: Ingrese solo números.")

def menu_sesion(usuario, cred, red):
    """Interfaz interna del usuario logueado."""
    while True:
        print(f"\n--- PERFIL DE {usuario} ---")
        print(f"Amigos: {len(red[usuario]['amigos'])} | Solicitudes: {len(red[usuario]['solicitudes'])}")
        print("1. Ver usuarios")
        print("2. Enviar solicitud")
        print("3. Ver solicitudes y aceptar")
        print("4. Ver mensajes")
        print("5. Enviar mensaje")
        print("6. Cerrar sesión")
        
        opc = validar_opcion(1, 6)
        
        if opc == 1:
            for u in red: print("-", u)
        elif opc == 2:
            destino = input("Destinatario: ")
            # Restricciones de la práctica[cite: 2]
            if destino not in red:
                print("No existe.")
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
            print("Tienes solicitudes de:")
            con=1
            c=False
            for i in red[usuario]["solicitudes"]:
                c=True
                print(f"{con}. {i}")
                con= con + 1
            if c == True:
                acep=input("¿Desea aceptar alguna solicitud?: ")
                if acep == "si":
                    acep=input("Ingrese el nombre del usuario: ")
                    red[usuario]["solicitudes"].remove(acep)
                    red[usuario]["amigos"].append(acep)
                    red[acep]["amigos"].append(usuario)
                    print("Amigo agregado")
                elif acep =="Si":
                    acep=input("Ingrese el nombre del usuario: ")
                    red[usuario]["solicitudes"].remove(acep)
                    red[usuario]["amigos"].append(acep)
                    red[acep]["amigos"].append(usuario)
                    print("Amigo agregado")
                elif acep == "no":
                    acep=input("¿Desea eliminar las solicitudes?: ")
                    if acep == "si":
                        for i in red[usuario]["solicitudes"]:
                                red[usuario]["solicitudes"].remove(i)
                    elif acep == "Si":
                        for i in red[usuario]["solicitudes"]:
                                red[usuario]["solicitudes"].remove(i)
                elif acep == "No":
                    acep=input("¿Desea eliminar las solicitudes?: ")
                if acep == "si":
                        for i in red[usuario]["solicitudes"]:
                            red[usuario]["solicitudes"].remove(i)
                elif acep == "Si":
                        for i in red[usuario]["solicitudes"]:
                            red[usuario]["solicitudes"].remove(i)
            else:
                print("No tienes solicitudes de amistad")
                
        elif opc == 4:
            # Los más recientes primero
            for m in red[usuario]["mensajes"]: print(m)
        elif opc == 5:
            destinatario=input("¿A quien desea enviarle el mensaje?: ")
            fecha_formateada = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            mns = f"El {fecha_formateada} {usuario} escribio: "
            """
            añadir fecha y hora en mns
            """
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

        elif opc == 6:
            break
        db.guardar_todo(cred, red)

def inicio():
    credenciales = db.cargar_usuarios()
    red = db.cargar_datos_red()
    
    while True:
        print("\n--- RED SOCIAL UDEA ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        
        opc = validar_opcion(1, 3)
        
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

if __name__ == "__main__":
    inicio()