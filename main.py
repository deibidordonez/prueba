import database as db
import datetime

def validar_opcion(min_val, max_val):
    """Validación de rango y tipo de dato mediante excepciones[cite: 1]."""
    while True:
        try:
            opc = int(input(f"Seleccione ({min_val}-{max_val}): "))
            if min_val <= opc <= max_val: return opc
            print("Fuera de rango.")
        except ValueError:
            print("Error: Ingrese solo números.")

def menu_sesion(usuario, cred, red):
    """Interfaz interna del usuario logueado[cite: 2]."""
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
            if destino not in red: print("No existe.")
            elif destino == usuario: print("No puedes enviarte a ti mismo.")
            elif destino in red[usuario]["amigos"]: print("Ya son amigos.")
            elif usuario in red[destino]["solicitudes"]: print("Ya enviada.")
            else:
                red[destino]["solicitudes"].append(usuario)
                print("Solicitud enviada.")
        elif opc == 4:
            # Los más recientes primero[cite: 1, 2]
            for m in red[usuario]["mensajes"]: print(m)
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