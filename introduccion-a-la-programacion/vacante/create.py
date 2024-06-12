import os

# contador_id = 1 # Generador manual de IDs

# el id se puedo configurar directamente en SQL como AUTO_INCREMENT y a medida que hacemos registros le asigna el id siguiente

def cargar_vacante():
    os.system('clear')
    print('\nDatos de la nueva vacante:\n')
    # titulo = input("Ingresá el título de la vacante: ")
    # descripcion = input("Ingresá una descripción: ")
    # condicion_contratacion = input(
    #     "Ingresá las condiciones de contratación (por tiempo indeterminado/determinado): ")
    # se_considera = input("Otras consideraciones del puesto:")
    # global contador_id
    # id = contador_id
    # contador_id += 1 # Incrementar el ID para la próxima vacante a agregar
    # vacantes[id] = {"titulo": titulo, "descripcion": descripcion, "id": id,
    #                 "condicion_contratacion": condicion_contratacion, "se_considera": se_considera}
    # print("Vacante agregada correctamente.")



# ------------------------------- CONECTAR CON DB ---------------------------------------

    '''import mysql.connector

    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    port='3306',
                                    database='data_humans.db')

    cursor = conexion.cursor()

    # Solo para plantear el problema, se ingresan datos str para darle al menos un dato a la sentencia de sql
    a = input()
    b = input()
    c = input()
    d = input()

    cursor.execute(f"INSERT INTO VACANTE/S VALUES ({a}, {b}, {c}, {d})")

    conexion.commit()

    conexion.close
'''
