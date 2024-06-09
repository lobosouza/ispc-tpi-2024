import os

def modificar_vacante():
    os.system('clear')
    print('\nModificar vacante por ID:\n')
    # id = int(input("Ingresá el ID de la vacante que querés modificar: "))
    # if id in vacantes:
    #     print("Datos actuales:", vacantes[id])
    #     modificar = input("¿Desea modificar los datos de esta vacante? (si/no): ")
    #     if modificar.lower() == "si":
    #         vacantes[id]["titulo"] = input("Ingresá el nuevo título (dejalo vacío para no modificar): ") or vacantes[id]["titulo"]
    #         vacantes[id]["descripcion"] = input("Ingresá la nueva descripción (dejalo vacío para no modificar): ") or vacantes[id]["descripcion"]
    #         vacantes[id]["condicion_contratacion"] = input("Ingresá la nueva condición de contratación (dejalo vacío para no modificar): ") or vacantes[id]["condicion_contratacion"]
    #         vacantes[id]["se_considera"] = input("Ingresá otros datos de la vacante (dejalo vacío para no modificar): ") or vacantes[id]["se_considera"]
    #         print("Vacante modificada correctamente.")
    #     else:
    #         print("No se han realizado modificaciones.")
    # else:
    #     print("La vacante con ese ID no existe en la base de datos.")