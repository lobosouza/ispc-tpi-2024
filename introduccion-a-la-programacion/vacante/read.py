import os

def ver_vacantes():
    os.system('clear')
    print('\nListado de vacantes:\n')
    # for id, datos in vacantes.items():
    #     print("ID:", id)
    #     print("Titulo:", datos["titulo"])
    #     print("Descripción:", datos["descripcion"])
    #     print("Condición de Contratación:", datos["condicion_contratacion"])
    #     print("Se considera:", datos["se_considera"])
    #     print("-" * 20, "\n")



# ------------------------------- CONECTAR CON DB ---------------------------------------
    '''import mysql.connector

    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    port='3306',
                                    database='data_humans.db')

    cursor = conexion.cursor()

    a = input()

    cursor.execute(f"SELECT * FROM VACANTE/S WHERE id_VACANTE/S = {a}")

    conexion.close()'''