from proxmoxer import ProxmoxAPI

proxmox = ProxmoxAPI('192.168.0.18', user='root@pam', password='usuario', verify_ssl=False)


def creaMaquina(idMaquina, nodo, imagen, nombre, memoria, sockets, cores, tamanio, storage ='local-lvm'):

    nuevaMaquina ={
        'vmid' : idMaquina,
        'name':nombre,
        'memory':memoria,
        'sockets':sockets,
        'cores':cores,
        'storage':storage,
        'cdrom':f'local:iso/{imagen}',
        'net0':'virtio,bridge=vmbr0' 
    }

    try:
        proxmox.nodes(nodo).qemu.create(**nuevaMaquina)
    except Exception as e:
        print(f"Error creando la VM: {e}")

def creaMaquinaPlantilla(idMaquina, nodo, idPlantilla, nombre, storage ='local-lvm'):
        
        try:
             proxmox.nodes(nodo).qemu(idPlantilla).clone.newid(vmid=idMaquina).name(nombre).target(nodo).storage(storage).create()
        except Exception as e:
             print(f"Error creando la VM: {e}")

def creaContenedor(idContenedor, contra, nodo, imagen, nombre, memoria, net0, sockets, cores, tamanio, rootfs, storage ='local-lvm'):
     
    nuevoContenedor = {
        'vmid':idContenedor,
        'ostemplate': imagen,
        'storage':storage,
        'hostname':nombre,
        'memory':tamanio,
        'cores':cores,
        'rootfs':rootfs,
        'net0':net0,
        'password':contra
    }
    try:
        proxmox.nodes(nodo).lxc.create(**nuevoContenedor)
    except Exception as e:print(f"Error creando el contenedor {e}")




def creaContenedorPlantilla():
    
    def creaContenedor(idContenedor, contra, nodo, idPlantilla, nombre, net0, cores, tamanio, rootfs,  storage ='local-lvm'):
        nuevoContenedor = {
            'vmid':idContenedor,
            'storage':storage,
            'hostname':nombre,
            'memory':tamanio,
            'cores':cores,
            'net0':net0,
            'password':contra
        }
         
        try:
            proxmox.nodes(nodo).lxc(idPlantilla).clone.create(**nuevoContenedor)
        except Exception as e:print(f"Error creando el contenedor {e}")



def mostrar_menu():
    print("\nMenú:")
    print("1. Crear máquina")
    print("2. Añadir contraseña")
    print("3. Borrar usuario")
    print("4. Salir")


def main():
    op = "0"

    while op != "4":
        mostrar_menu()
        op = input("Selecciona una opción: ")

        if op == '1':
            idMaquina = input("Introduzca el id: ")
            nodo = input("Introduzca el nodo: ")
            imagen = input("Introduzca la imagen: ")
            nombre = input("Introduzca nombre: ")
            memoria = input("Introduzca memoria: ")
            sockets = input("Introduzca sockets: ")
            cores = input("Introduzca cores: ")
            tamanio = input("Introduzca el tam: ")
            storage ='local-lvm'
            creaMaquina(idMaquina, nodo, imagen, nombre, memoria, sockets, cores, tamanio, storage)
        elif op == '2':
            print("to do")
            #nombre = input("Introduzca el nombre del usuario: ")
            #pas = input(f"Introduzca una contraseñapara el usuario {nombre}: ")
            #creaContra(nombre,pas)
        elif op == '3':
            print("to do")
        elif op == '4':
            input("Pulse enter para salir del programa")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()