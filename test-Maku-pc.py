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

#print(readRow())

def readLast():
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"SELECT DISTINCT num_reservacion FROM reservas ORDER BY num_reservacion DESC LIMIT 3"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

# print(int(readLast()))

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

def asientos(n, h):
    c=f"SELECT COUNT(teleferico) FROM reservas WHERE teleferico={n} AND horaio = {h}"
    return consultar(c)[0][0] #ej [(6,)]

# print(asientos(1,1))

def datos_factura(r):
    c=f"SELECT nombre, edad, nacionalidad, num_reservacion FROM reservas WHERE num_reservacion={r}"
    return consultar(c)

#print(datos_factura(4))

total=0
for r in datos_factura(4):
    nombre = r[0]
    edad = r[1]
    codigo_nacionalidad = r[2]
    if codigo_nacionalidad == 1:
        nacionalidad = "Nacional"
    else:
        nacionalidad = "Extrangero"
    monto = 0
    if 65 > edad > 18 and codigo_nacionalidad == 2:
        monto = 7000
    elif 65 > edad > 18 and codigo_nacionalidad == 1:
        monto = 5000
    elif codigo_nacionalidad == 2:
        monto = 3500
    else:
        monto = 2500
    total+=monto
    print((nombre)+",",edad,"años\t\t", nacionalidad,"\t",monto)
iva = round(total*0.13)
print("\t\t\t\tIva\t",iva)
print("\t\t\t\tTOTAL\t", total+iva)

def readLast1():
    q = f"SELECT DISTINCT num_reservacion FROM reservas ORDER BY num_reservacion DESC LIMIT 2"
    x = consultar(q)
    if x:
        return x[0][0]
    else:
        return 0

#print(readLast1())
lista = [
    (4,"Marco",1,29,1,1,1,"10/07/2022"),
    (4,"Diego",1,29,1,1,1,"10/07/2022"),
    (4,"Juan",1,29,1,1,1,"10/07/2022"),
    (4,"Gustavo",1,29,1,1,1,"10/07/2022")
]

# i = input("  [ N ] Nueva Factura    [ ⏎ ] Menu    [ X ] Salir\n")
# if i == "x" or "X":
#     exit()
# print("Menu")

#insertRows(lista)
#print(readRow())

def personas_horario(h):
    c=f"SELECT COUNT(teleferico) FROM reservas WHERE horario = {h}"
    return consultar(c)

#print(personas_horario(1))

def contar_tarifa_Adultos(n):
    c=f"SELECT COUNT(teleferico) FROM reservas WHERE nacionalidad={n} AND edad  < 65 AND edad >18"
    return consultar(c)

def contar_tarifa_Ninos_Mayores(n):
    c=f"SELECT COUNT(teleferico) FROM reservas WHERE nacionalidad={n} AND edad  > 65 OR edad < 18"
    return consultar(c)

# print(contar_tarifa_Adultos(1))
# print(contar_tarifa_Ninos_Mayores(1))

def horario_mayor():
    c=f"SELECT COUNT(asiento), horario FROM reservas GROUP BY horario ORDER BY COUNT(asiento) DESC LIMIT 1"
    return consultar(c)

# print(horario_mayor())


#print(
"""
----------+--------+--------------+--------+---------+------------+---------+--------+
| reserva | nombre | nacionalidad |  edad  | horario | teleferico | asiento | fecha  |
----------+--------+--------------+--------+---------+------------+---------+--------+
| [0][1]  | [0][2] | [0][3]       | [0][4] | [0][5]  | [0][6]     | [0][7]  | [0][8] |
| [1][1]  | [1][2] | [1][3]       | [1][4] | [1][5]  | [1][6]     | [1][7]  | [1][8] |



  +--------------------------------------------------------------+
  |                     AVENTURAS EL PARAISO                     |
  +--------------------------------------------------------------+
  | Reservacion n°5                                 Horario: 8am |
  | Cliente: Marco Antonio Aguilar                   1-1528-0607 |
  ================================================================
  |                                                              |
  |    DETALLE                        TARIFA              MONTO  |
  | Marco, 29 años            Extrangero Adulto Mayor   $   5000 |
  | Marco, 29 años            Nacional Adulto           $ 115000 |
  | Marco, 29 años            Extrangero Adulto         $   5000 |
  | Anthonio, 29 años         Nacional Niño             $ 115000 |
  |                                               IVA   $    130 |
  +                                                              +
  | 9 personas                                   TOTAL  $  10000 |
  +--------------------------------------------------------------+
  |                  Gracias por su visita                       |
  +--------------------------------------------------------------+


══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
║  First name            ║  Last name             ║  email                 ║  Address Line 1        ║  city                  ║  
══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
║  Hillier               ║  O'Howbane             ║  hohowbane0@gmpg.org   ║  6960 New Castle Driv  ║  Monte de Frales       ║  
║  Micheal               ║  Matevosian            ║  mmatevosian1@arizona  ║  2 Tennessee Drive     ║  Longchiqiao           ║  
║  Eba                   ║  Cardinale             ║  ecardinale2@hhs.gov   ║  62 Hoard Junction     ║  Mae Fa Luang          ║  
║  Yardley               ║  Doiley                ║  ydoiley3@meetup.com   ║  9961 Sachs Park       ║  Tromsa                ║  
║  Jeannette             ║  Bartlet               ║  jbartlet4@washington  ║  5 Sheridan Avenue     ║  Dhanot                ║  
║  Ellerey               ║  Faircliffe            ║  efaircliffe5@sina.co  ║  881 Donald Place      ║  Taumatawhakatangi­ha  ║  
║  Carolin               ║  Hefner                ║  chefner6@t.co         ║  22261 Carioca Road    ║  Candating             ║  
║  Kamilah               ║  Childrens             ║  kchildrens7@theglobe  ║  8418 Talisman Way     ║  Bacabal               ║  
║  Rosana                ║  Penella               ║  rpenella8@is.gd       ║  66435 Twin Pines Way  ║  General Viamonte      ║  
║  Lynnette              ║  Kollasch              ║  lkollasch9@cargocoll  ║  32439 Novick Avenue   ║  Tashang               ║  
║  Alejandra             ║  De Cristoforo         ║  adecristoforoa@delic  ║  7 Eastlawn Lane       ║  Sintung Timur         ║  
║  Sheila-kathryn        ║  Weatherell            ║  sweatherellb@joomla.  ║  4527 Caliangt Place   ║  Markovo               ║  
║  Bancroft              ║  Eastwood              ║  beastwoodc@purevolum  ║  0925 Jackson Terrace  ║  Lalala                ║  
║  Zackariah             ║  Sinnock               ║  zsinnockd@skype.com   ║  683 Duke Drive        ║  Gerelayang            ║  
║  Wilma                 ║  Scogin                ║  wscogine@zdnet.com    ║  15 Graceland Crossin  ║  Gununggoong           ║  
║  Petronia              ║  Dradey                ║  pdradeyf@bigcartel.c  ║  96394 Hollow Ridge P  ║  Desa Nasol            ║  
║  Sherri                ║  Ecclestone            ║  secclestoneg12232_32  ║  0948 Ludington Parkw  ║  Lameiro               ║  
║  Niven                 ║  Felgat                ║  nfelgath@europa.eu    ║  12 Crownhardt Place   ║  Greensboro            ║  
║  Alysia                ║  Macari                ║  amacarii@newsvine.co  ║  93 Ridge Oak Plaza    ║  Dobrljin              ║  
║  Cody                  ║  Mounsey               ║  cmounseyj@delicious.  ║  7299 Eastlawn Alley   ║  Castro                ║  
══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

