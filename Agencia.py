clientes = {}
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
    clientes[codigo]["edad"] = int(input("Ingrese el edad del cliente: "))
    clientes[codigo]["telefono"] = input("Ingrese el telefono del cliente: ")
    clientes[codigo]["correo"] = input("Ingrese el correo del cliente: ")
    print("¿Cuántos destinos ha visitado el cliente?: ")
    dest = int(input())
    while True:
        if dest > 0:
            for j in range(dest):
                print(f"Destino #{j+1}: ")

        else:
            print("La cantidad de destinos debe ser mayor a 0")