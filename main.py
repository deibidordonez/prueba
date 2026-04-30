archivo = open("users.txt", "r", encoding = "utf 8")
archivo2 = open("userData.txt", "r")
import Funciones as f
usu = f.cargar_usuarios(archivo)
usu_a= f.guardar_usuarios(usu)
print(usu_a)
