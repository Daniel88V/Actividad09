clientes = {}
destinos = []
print("¿Cuántos clientes desea ingresar?: ")
cant = int(input())
for i in range(cant):
    print(f"Cliente #{i +1}: ")
    while True:
        codigo = input("Ingrese el código del cliente: ")
        clientes[codigo] = {}
        if codigo in clientes:
            print("Error, este cliente ya fue registrado")
        else:
            break
    clientes[codigo]["nombre"] = input("Ingrese el nombre del cliente: ")
    """
    clientes[codigo]["edad"] = int(input("Ingrese el edad del cliente: "))
    clientes[codigo]["telefono"] = input("Ingrese el telefono del cliente: ")
    clientes[codigo]["correo"] = input("Ingrese el correo del cliente: ")
    """
    print("¿Cuántos destinos ha visitado el cliente?: ")
    dest = int(input())
    while True:
        if 0 < dest <= 5 :
            for j in range(dest):
                visitas = input(f"Destino #{j+1}: ")
                destinos.append(visitas)
            break
        else:
            print("La cantidad de destinos debe ser mayor a 0 y menor que 6")
print("¿Desea realizar alguna de las siguientes")