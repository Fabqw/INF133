import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("instituto.db")

print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)