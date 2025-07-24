clientes = {}
destinos = []
print("¿Cuántos clientes desea ingresar?: ")
cant = int(input())
for i in range(cant):
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

print("¿Desea realizar alguna de las siguientes ")