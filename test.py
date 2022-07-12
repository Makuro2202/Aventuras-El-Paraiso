import sqlite3

def insertRow(numResvacion, nombre, nacionalidad, edad, horario, teleferico, asiento, fecha):
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"INSERT INTO reservas VALUES (NULL,{numResvacion},'{nombre}',{nacionalidad},{edad},{horario},{teleferico},{asiento},'{fecha}')"
    cursor.execute(query)
    conn.commit()
    conn.close()

def readRow():
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM reservas"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def readLast():
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"SELECT DISTINCT num_reservacion FROM reservas ORDER BY num_reservacion DESC LIMIT 3"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def countEntris():
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"SELECT COUNT(num_reservacion) FROM reservas WHERE num_reservacion=3 AND nombre like 'Diego';"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def insertRows(mylist):
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"INSERT INTO reservas VALUES (null,?,?,?,?,?,?,?,?)"
    cursor.executemany(query, mylist)
    conn.commit()
    conn.close()


#insertRow(3,"Diego",1,29,1,1,1,"10/07/2022")
# print(readRow())
# print(readLast())
#print(countEntris())

def espacios_disponibles(num_horario):
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"SELECT COUNT(num_reservacion) FROM reservas WHERE horario = {num_horario}"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos[0][0]
#x=18-espacios_disponibles(1)
# print(espacios_disponibles(1))
# print(18-int(espacios_disponibles(1)))


def conteoTeleferico():
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    #query = f"SELECT COUNT(teleferico), teleferico FROM reservas GROUP BY teleferico ORDER BY COUNT(teleferico) "
    query = f"SELECT COUNT(teleferico), teleferico FROM reservas GROUP BY teleferico"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos
    
# print(conteoTeleferico())

def asientos_teleferico(n):
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"SELECT COUNT(teleferico) FROM reservas WHERE teleferico={n}"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

# print(asientos_teleferico(1))

def consultar(query):
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def asientos(n):
    c=f"SELECT COUNT(teleferico) FROM reservas WHERE teleferico={n}"
    return consultar(c)[0][0] #ej [(6,)]

print(asientos(1))
lista = [
    (4,"Marco",1,29,1,1,1,"10/07/2022"),
    (4,"Diego",1,29,1,1,1,"10/07/2022"),
    (4,"Juan",1,29,1,1,1,"10/07/2022"),
    (4,"Gustavo",1,29,1,1,1,"10/07/2022")
]


#insertRows(lista)
#print(readRow())