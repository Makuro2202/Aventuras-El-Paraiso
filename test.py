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
print(countEntris())

lista = [
    (4,"Marco",1,29,1,1,1,"10/07/2022"),
    (4,"Diego",1,29,1,1,1,"10/07/2022"),
    (4,"Juan",1,29,1,1,1,"10/07/2022"),
    (4,"Gustavo",1,29,1,1,1,"10/07/2022")
]

#insertRows(lista)
#print(readRow())