import mysql.connector
from pprint import pprint #pprint es preety print, sirve para imprimir una lista/diccionario de forma ordenada

#def obtener_conexion():

try:
#1. Configurar las credenciales
    conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbinstituto"
    )

#2. Verificar la conexión
    if conexion.is_connected():
        #Crear el cursor
        cursor = conexion.cursor(dictionary=True)

        #Definir y ejecutar la consulta
        query = "SELECT * FROM tbl_estudiantes;" #se pone entre comillas porque la orden a mysql se envía como string.
        cursor.execute(query)

        #Obtener los resultados
        registros = cursor.fetchall() #esta variable es un diccionario y fetchall devuelte una lista con multiples elementos.

        #Imprimir diccionario
        for registro in registros:
           pprint(registro)

     #print("Conexión exitosa con MYSQL")
    #else:
        #print("Error")

except mysql.connector.Error as err:
   print(f"Error al conectar: {err}")

finally: #finally es un comando que sirve para que al final se ejecute la orden sí o sí
   #3. Cerrar la conexión
   if 'conexion' in locals() and conexion.is_connected():
    conexion.close()
    print("Conexión cerrada")


