import mysql.connector # Conectar a la base de datos
from getpass import getpass  # no se puede ver la contrasenia

connection = mysql.connector.connect(user='root',
                                    password='root',
                                    port='3306',
                                    host='localhost',
                                    database="datahumans_db"
                                    )
cursor = connection.cursor()


def login():
    print("Ingrese usuario y contraseña para ingresar al sistema")

    try:
        consulta = """
                    SELECT nombreUsuario, clave 
                    FROM usuarios 
                    WHERE nombreUsuario = %s AND clave = %s 
                    """ 
        
        Usuario = input("nombre de usuario ")
        pwd = input("contraseña ")

        # Ejecutar la consulta con los valores proporcionados
        cursor.execute(consulta, (Usuario, pwd))
        
        resultados = cursor.fetchall()
        
        if resultados:
            print("Bienvenid@!")
        else:
            print("Usuario o contraseña incorrectos.")


    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        connection.rollback()

# Llamar a la función para registrar el usuario
login()

# Cerrar la conexión
cursor.close()
connection.close()