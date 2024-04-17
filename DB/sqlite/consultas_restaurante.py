import sqlite3

#Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

#Encuentra todos los pedidos realizados junto con los nombres de los platos y los números de mesa (JOIN)
print("------ Primer ejercicio -----")
cursor = conn.execute(
   """
   SELECT PEDIDOS.ID, PLATOS.NOMBRE, MESAS.NUMERO
   FROM PEDIDOS
   JOIN PLATOS ON PLATOS.ID = PEDIDOS.PLATO_ID
   JOIN MESAS ON MESAS.ID = PEDIDOS.MESA_ID
   """
)
for row in cursor:
   print(row)

print("------ Segundo ejercicio -----")
#Encuentra todos los platos que han sido pedidos, incluso aquellos que no se han pedido aún (LEFT JOIN)
cursor = conn.execute(
    """
    SELECT PL.*, PEDIDOS.ID 
    FROM PLATOS AS PL
    LEFT JOIN PEDIDOS ON PL.ID = PEDIDOS.PLATO_ID
    """
)
for row in cursor:
    print(row)
    

conn.commit()
conn.close()
