import sqlite3

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