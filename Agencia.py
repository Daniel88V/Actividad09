clientes = {}
print("¿Cuántos clientes desea ingresar?: ")
cant = int(input())
for i in range(cant):
    destinos = []
    print(f"Cliente #{i +1}: ")
    while True:
        codigo = input("Ingrese el código del cliente: ")
        if codigo in clientes:
            print("Error, este cliente ya fue registrado")
        else:
            break
    nombre = input("Ingrese el nombre del cliente: ")
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
    clientes[codigo] = {
        "nombre": nombre,
        "destino":{
            "lugares": destinos
        }
    }

print("¿Desea realizar alguna de las siguientes opciones?")
print("1. Desplegar listado de clientes")
print("2. Desplegar el total de destinos visitados")
print("3. Desplegar el cliente con más destinos visitados")
print("4. Salir")
print("Seleccione una opción: ")
opcion = input()
if opcion == "1":
    print("\t ---Listado de clientes---")
    for codigo, datos in clientes.items():
        print(f"Codigo: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Destinos: {datos['destino']['lugares']}")
elif opcion == "2":
    print("\t ---Cantidad de destinos visitados---")
