import os


def eliminar_vacante():
    os.system('clear')
    print('\nEliminar vacante por ID:\n')
    # id = int(input("Ingresá el ID de la vacante que querés eliminar: "))
    # if id in vacantes:
    #     del vacantes[id]
    #     print("Vacante eliminada correctamente.")
    # else:
    #     print("La vacante con ese ID no existe en la base de datos.")




# ------------------------------- CONECTAR CON DB ---------------------------------------
    '''import mysql.connector

    #CONECTA CON DB
    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    port='3306',
                                    database='data_humans.db')
    cursor = conexion.cursor()

    a = input() # se crea solo para darle un parametro a la sentencia

    # BORRA DATOS SEGúN CONDICIÓN, SI NO SE PONE CONDICIÓN BORRA TODA LA TABLA
    cursor.execute(f"DELETE FROM VACANTE/S WHERE id_VACANTE/S = {a}")

    conexion.commit()

    conexion.close()
'''