


import sys
sys.path.append("/Users/apple/Desktop/python_tutorial/otro")

from hello import users


usuarios = users

rta = "y"
while rta !='3':

    print("Bienvenido al sistema de gestión")
    
    
    for key in usuarios:
        print(key," ",usuarios[key])

    print("\n1. Agregar")
    print("2. Eliminar")
    print("3. Salir")

    rta = input('Ingrese opcion: ')

    if rta == '1':

        ced = input('Ingrese cedula')
        nombre = input('Ingrese nombre')
        usuarios[ced]=nombre
        

    if rta == '2':

        ced = input('Ingrese cedula a eliminar')
        try:
            usuarios.pop(ced)
        except (ValueError,KeyError):
            print("Oops!  No es un numero valido")
            temp = input('Ingrese cualquier tecla para continuar...')

            continue
        