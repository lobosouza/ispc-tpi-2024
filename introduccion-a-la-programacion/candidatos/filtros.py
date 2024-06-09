import os

def filtrar_por_requisitos():
    os.system('clear')
    print('\nFiltrar por:\n')


'''
# en esta funcion podriamos pasarle como argumento el ID de la vacante que debe comparar y retornar los resultados de las coincidencias
# en esta propuesta usé SQLite que ya viene con python, pero hay que modificar el import y la conexion para usar MySQL
def filtrar_por_requisitos():

    import os

    import sqlite3

    os.system('clear')

    # define lista para almacenar las posibles coincidencias
    coincidencias = []

    print('\nFiltrar por:\n')

    print('COINCIDENCIAS')

    # se ingresa ID de la vacante para buscar posibles coincidencias
    print('Ingresa el ID de la vacante para ver los candidatos que cumplen los requisitos')
    vacante_id = str(input('ID:'))

    conexion = sqlite3.connect("base_de_datos.db") # conecta con bd
    
    cursor = conexion.cursor() # Crea cursor para poder poder ejecutar sentencias de SQL
    
    cursor.execute("SELECT * FROM VACANTE/S WHERE Id_VACANTE/S = " + str(vacante_id)) # realiza la consulta para la entidad "VACANTE/S".
    
    vacante = cursor.fetchall() # almacena los resultados obtenidos en variable, esta info obtenida se usaria para hacer las comparaciones
    # de los requerimientos para el puesto y también mostramos en pantalla los detalles de la vacante

    cursor.execute("SELECT * FROM POSTULANTE") # realiza la consulta para la entidad "POSTULANTE".
    
    postulantes = cursor.fetchall() # almacena los resultados obtenidos en variable, queda como una  lista de tuplas

    # Se supone que por cada elemto devuelve una tupla: (id_postulante, dni, nombre, apellido, fecha_nacimiento, recidencia, nivel_academico, cv, puesto_deseado)
    # Fecha_nacimiento la asumimos como edad (Despues hacemos el cálculo anios = fecha_actual - fecha_nacimiento)

    conexion.close() 

    
    for postulante in postulantes: # Itera sobre la lista obtenida de la consulta a la DB
        
        # Primero deberíamos comparar los requisitos excluyentes brindados por cada puesto en particular
        # Por ahora solo planteo la comparación con los requisitos básicos de la consigna: mayor de 18 años, vivir en ciudad de Córdoba y secundario completo
        if postulante[4] >= 18 and postulante[5] == 'cordoba' and postulante[6]: #el nivel_academico lo asumo como un valor lógico, secundario_completo = True/False
            coincidencias.append(postulante)

    # muestra cada coincidencia en consola
    for i in coincidencias:
        print(i)

'''