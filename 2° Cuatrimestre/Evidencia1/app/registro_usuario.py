import mysql.connector
from getpass import getpass  # no se puede ver la contrasenia
import captcha

# Conectar a la base de datos
connection = mysql.connector.connect(user='root',
                                    password='root',
                                    port='3306',
                                    host='localhost',
                                    database="datahumans_db"
                                    )
cursor = connection.cursor()

# Función de verificación con captcha
def verificacion():

    if captcha.verificar_captcha():
        try:
            connection.commit()
            print("Usuario registrado con éxito.")
        except mysql.connector.Error as err:
            print(f"Error: {err}") 
            connection.rollback()
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            connection.rollback()
    else:
        print("Algo está mal, inténtalo nuevamente")
        verificacion()

# Función para registrar un usuario
def registrar_usuario():
    print("Por favor, ingrese los siguientes datos del usuario:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    correo_electronico = input("Correo Electrónico: ")
    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
    nombreUsuario = input("Nombre de Usuario: ")
    clave = getpass("Clave: ")  # contrasenia oculta

    # Comando SQL para insertar los datos en la tabla 'usuarios'
    sql = """
    INSERT INTO usuarios (nombre, apellido, dni, correo_electronico, fecha_nacimiento, nombreUsuario, clave)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    # Ejecutar la consulta con los valores proporcionados
    cursor.execute(sql, (nombre, apellido, dni, correo_electronico, fecha_nacimiento, nombreUsuario, clave))

    #verificar usuario con captcha
    verificacion()


# Llamar a la función para registrar el usuario
#registrar_usuario()

# Cerrar la conexión
cursor.close()
connection.close()
