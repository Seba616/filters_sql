import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',          # reemplaza con tu usuario MySQL
    password='diminombre.85',   # reemplaza con tu contraseña
    database='tienda'
)
cursor = cnx.cursor()
