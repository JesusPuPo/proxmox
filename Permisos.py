from proxmoxer import ProxmoxAPI

# Conexión con el proxmox
#Importante el @pam, si no da error de conexion
proxmox = ProxmoxAPI('192.168.90.176', user='root@pam', password='usuario', verify_ssl=False)


def asignaRol(idUsuario, nombreRol):

    nuevoUsuarioRoll = {
        'path': '/',
        'roles': nombreRol,
        'users': idUsuario
    }

    try:

        proxmox.access.acl.set(**nuevoUsuarioRoll)

    except Exception as e:
        print(f"Error al asignar el rol a '{idUsuario}': {str(e)}")

def asignaGrupo(idGrupo, idUsuario):

    grupoAsignado = {
        'userid' : idUsuario,
        'groups' : idGrupo
    }

    try:
        proxmox.access.users.update(**grupoAsignado)
        print(f"Usuario {idUsuario} agregado al grupo {idGrupo}.")
    except Exception as e:
        print(f"Error agregando usuario al grupo: {e}")

def asignaPool(pool, idUsuario):
    try:
        proxmox.pools(pool).update(users=f'{idUsuario}')
        print(f"Usuario {idUsuario} asignado al pool {pool}.")
    except Exception as e:
        print(f"Error asignando el usuario al pool: {e}")
