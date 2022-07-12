import sqlite3

#FUNCION CONSULTAR
def consultar(query):#el parmetro query almacenara la consulta
    conn = sqlite3.connect("elParaiso.db") # con connect nos conecta con la base de datos
    cursor = conn.cursor() # el cursor "selecionara" los registros que le indiqueca la consulta
    cursor.execute(query) # ejecuta lo que le pasa el parametro query (la consulta)
    datos = cursor.fetchall() # fetchall pasa la infomacion a la variable datos
    conn.close() # cerramos la coneccion con la base de datos
    return datos

#la funcion espacios disponibles devuelve cuantos asientos hay para un determinado horario 
# 1 es el horario de las 8:00 am
# 2 es el horario de las 10:00 am
# 3 es el horario de las 12:00 md
# 4 es el horario de las 2:00 pm

def espacios_disponibles(numero_de_horario):
    q = f"SELECT COUNT(asiento) FROM reservas WHERE horario = {numero_de_horario}"
    #q cuenta los asientos de un horario dado
    t = 18 #numero total de espacios por horario 6 pasajeros 3 telefericos 18
    o = consultar(q)[0][0] #asientos ocupados ej de la respuesta sin el [0][0] >>>[(6,)]
    return t-o #total menos ocupados da los disponibles

# print(espacios_disponibles(1))


# la funcion asientos devuelve el numero de asientos de un teleferico n
def asientos(n):
    q=f"SELECT COUNT(teleferico) FROM reservas WHERE teleferico={n}"
    # coenta cuantas veces aparece un registro en la tabla reservas de un teleferico n
    return consultar(q)[0][0] #ej de la respuesta sin el [0][0] >>>[(6,)]

#print(asientos(1))