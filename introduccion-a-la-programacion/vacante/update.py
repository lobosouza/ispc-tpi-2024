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




# ------------------------------- CONECTAR CON DB ---------------------------------------
    '''import mysql.connector

    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    port='3306',
                                    database='data_humans.db')

    cursor = conexion.cursor()

    a = input()
    b = input()

    cursor.execute (f"UPDATE VACANT/S SET algo = {a} WHERE algo = {b}'") # Esto solo es un ejemplo, falta desarrollar segun condiciones

    conexion.commit()
    conexion.close()'''