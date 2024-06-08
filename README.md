# GRUPO N° 23

<div id="top"></div>

<div align="center">
<h3 align="center">Evidencia 2: Sistema de Gestión de Empleados para Recursos Humanos</h3>
 <p align="center">
    Proyecto: DATA  HUMAN´S
    <br />
    VER ÍNDICE MÁS ABAJO
    <br />
    <br />
  </p>
</div>

<!-- INDICE -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#integrantes">Integrantes</a>
    </li>
    <li><a href="#introduccion-a-la-programación">Introducción a la programación</a>
     <ul>
        <li><a href="#presentación">Presentación del proyecto</a></li>
        <li><a href="#descripción">Descripción inicial</a></li>
        <li><a href="#pseudocodigo">Pseudocódigo</a></li>
      </ul>
    </li>
    <li><a href="#etica">Etica y Deontología Profesional</a></li>
        <li><a href="#bbdd">Base de datos</a></li>
  </ol>
</details>

<br />
<br />

<!-- INTEGRANTES -->

# Integrantes

Carolina Araque - 30.721.217 - carolinaaraq@gmail.com - https://github.com/Caroaraque2024 </br>
Joaquin Dorgnach - 45.704.025 - dorgnachj@gmail.com - https://github.com/dorgnachj</br>
Lucas Ryser - 44.346.194 - lucasryser4k@gmail.com - https://github.com/lucasryser6</br>
Emanuel Guaráz - 38.276.061- guarazjemanuel@gmail.com https://github.com/JEmanuelG</br>
Nicolás Allende Olmedo - 35.871.057 - nicoallende92@gmail.com - https://github.com/AllendeNicolas</br>
Rocío Girardini - 41.280.222 - rogirardini@gmail.com - https://github.com/rociogirardini</br>

<h3 align="center" id="introduccion-a-la-programación">Introducción a la programación</h3>

<h4 id='presentación'><strong>PRESENTACIÓN</strong></h4>

<p>DATA HUMAN´S, es una empresa dedicada al desarrollo y mantenimiento de Software y Bases de Datos, orientada a la organización y asistencia de los departamentos de Recursos Humanos (RRHH), de las empresas en general.</p>

<p>Brindamos un sistema de Bases de Datos y Gestión de empleados, el cual cuenta con un sistema de selección de personal, mediante filtros de búsqueda entre los posibles candidatos, para los puestos vacantes de las empresas, ajustandose a las necesidades y requisitos a cumplir para el ingreso a planta.</p>

<p>Cuenta también, con un análisis de producción de cada empleado, considerando las tareas que debe realizar, analizando su eficacia, y eficiencia laboral. También un análisis del ambiente laboral, teniendo en cuenta las relaciones interpersonales de los empleados dentro de la planta, y considerando la salud mental (aptos psicológicos) de los integrantes de la empresa.</p>

<p>Entre otras funciones básicas, podemos encontrar, conteos de empleados en planta, alta y baja de los mismos, filtros por departamentos, asignaciones de indumentaria laboral, pagos de sueldos, aportes y seguridad social, verificación de asistencia laboral, etc.</p>

<p>(La descripción anterior, es a lo que nos gustaría llegar, como proyecto final).</p>

<h4 id='descripción'><strong>DESCRIPCIÓN INICIAL DEL PROYECTO</strong></h4>

En esta parte inicial del proyecto, proponemos realizar un sistema de selección de personal básico, para una empresa de limpieza. Donde el aspirante debe cumplir con los siguientes requisitos:

- Ser mayor de edad (+18 años).
- Residir en la Ciudad de Córdoba.
- Tener estudios secundarios completos.

<h4 id='pseudocodigo'><strong>PSEUDOCÓDIGO</strong></h4>

<p align="center"><a href="https://github.com/rociogirardini/ispc-tpi-2024/tree/main/introduccion-a-la-programacion"><strong>Ver pseudocódigo »</strong></a></p>

<h4 id='descripcion-archivos'><strong>DESCRIPCIÓN DE LOS ARCHIVOS</strong></h4>

#### `index.py` 

<p>Este archivo contiene el punto de entrada de la aplicación y la función principal `seleccion_personal()`, que maneja el menú y las opciones del usuario.</p>

<h4> <strong> 📂 Carpeta `candidatos` </strong> </h4>

<p>Contiene los archivos:</p>

#### `candidatos.py`

<p>Este módulo contiene una función llamada `ver_candidatos()`, la cual permite ver una lista detallada de todos los candidatos existentes en la base de datos.</p>

#### `filtros.py`

<p>Acá se encuentra la función `filtrar_por_requisitos()` donde el usuario podría ingresar ciertas características del candidato, como lugar de residencia, experiencia o educación y la función mostraría solo aquellos candidatos que coincidan con los filtros de búsqueda.</p>

<h4> <strong> 📂 Carpeta `vacante` </strong> </h4>

<p>Contiene los archivos del CRUD de una vacante:</p>

#### `create.py`

<p>Contiene la función `cargar_vacante()` donde se le solicitarían al usuario todos los datos relacionados a la vacante, tales como título del puesto, descripción, condiciones de contratación, entre otros.</p>

#### `read.py`

<p>En este archivo se encuentra la función `ver_vacantes()`, que traería un listado de todas las vacantes disponibles.</p>

#### `update.py`

<p>Contiene la función `modificar_vacante()` donde el usuario, mediante el previo ingreso del ID de la vacante que desea modificar, podría modificar cualquiera de sus datos.</p>

#### `delete.py`

<p>Acá se encuentra la función `eliminar_vacante()` donde el usuario debe ingresar el ID de la vacante que desea eliminar para que esta sea quitada de la base de datos.</p>



<h3 align="center" id="etica">Etica y Deontología Profesional</h3>
<p align="center"><a href="https://github.com/rociogirardini/ispc-tpi-2024/wiki"><strong>Ver Wiki »</strong></a></p>

<h3 align="center" id="bbdd">Base de datos I</h3>
<p align="center"><a href="https://github.com/rociogirardini/ispc-tpi-2024/blob/main/base-de-datos-1/diagrama_entidad_relacion.jpg"><strong>Ver Diagrama Entidad - Relación »</strong></a></p>
