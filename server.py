from flask import Flask, render_template, request
import mysql.connector
from cnx_sql import cursor

app = Flask(__name__)


@app.route('/productos', methods=['GET'])
def filtrar_productos():
    # Leer filtros del query string
    talla = request.args.get('talla')          # p.ej. 'M', 'L', etc.
    marca = request.args.get('marca')          # p.ej. 'MarcaA'
    precio_min = request.args.get('precio_min', type=float)  # convierte a float
    precio_max = request.args.get('precio_max', type=float)

    # Construir consulta SQL dinámicamente
    query = "SELECT id, nombre, talla, precio, marca FROM productos WHERE 1=1"
    params = []
    if talla:
        query += " AND talla = %s"
        params.append(talla)
    if marca:
        query += " AND marca = %s"
        params.append(marca)
    if precio_min is not None:
        query += " AND precio >= %s"
        params.append(precio_min)
    if precio_max is not None:
        query += " AND precio <= %s"
        params.append(precio_max)

    cursor.execute(query, params)  # Uso de placeholders y parámetros
    resultados = cursor.fetchall()
    return render_template('productos.html', productos=resultados)

if __name__ == "__main__":
    app.run(debug=True)


