from proxmoxer import ProxmoxAPI

# Conexión con el proxmox
#Importante el @pam, si no da error de conexion
proxmox = ProxmoxAPI('192.168.90.176', user='root@pam', password='usuario', verify_ssl=False)

# Define la función para crear un usuario
def crear_usuario(nombre_usuario, correo_usuario):
    try:
        # Define los parámetros del nuevo usuario
        nuevo_usuario = {
            'userid': nombre_usuario,
            'email': correo_usuario,
            'enable': 1,
            'comment': f'Usuario creado mediante script de Python'
        }
        
        #Crea el usuario enviando un json al endpoint de la API de proxmox
        proxmox.access.users.create(**nuevo_usuario)
        
        print(f"Usuario '{nombre_usuario}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear usuario '{nombre_usuario}': {str(e)}")
        
        #############################
        # 
        #La contraseña no va, revisar
        #
        #https://pve.proxmox.com/pve-docs/api-viewer/#/access/password
        #        
        #PUT /api2/json/access/password
        #
        ############################

def main(args):
    nombre_usuario = input("Nombre de usuario: ")
    contrasena_usuario = input("Contraseña: ")
    correo_usuario = input("Correo electrónico: ")
    
    crear_usuario(nombre_usuario, correo_usuario)
