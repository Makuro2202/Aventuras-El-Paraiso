# PROJECTO FINAL GRUPO 01. UNIVERSIDAD FIDELITAS
from ast import Pass
import sqlite3

def separator():
    x="-"*60
    return x
def menu():
    menu = """
    ===============================================
      /_\ \ / / __| \| |_   _| | | | _ \  /_\ / __|
     / _ \ V /| _|| .` | | | | |_| |   / / _ \\__  \ 
    /_/_\_\_/ |___|_|\_| |_|  \___/|_|_\/_/ \_\___/
    | __| |    | _ \/_\ | _ \  /_\ |_ _/ __|/ _ \  
    | _|| |__  |  _/ _ \|   / / _ \ | |\__ \ (_) | 
    |___|____| |_|/_/ \_\_|_\/_/ \_\___|___/\___/               
    ===============================================
    ----------------  Bienvenido!  ----------------
    """    
    print(menu)
    return menu_de_seleccion()   

def menu_de_seleccion():
    print("""Menu de usuario, seleccione el modulo al que desea acceder

    \t[1] Reservación
    \t[2] Facturación
    \t[3] Informes
    \t[4] Salir
    """)
    print(separator())
    seleccion = int(input("Digite una opcion: "))
    if seleccion == 1:
        try:
            reservas()
        except:
            print("Error modo Reservas")
    elif seleccion == 2:
        try:
            facturacion()
        except:
            print("Error modo facturación")
    elif seleccion == 3:
        try:
            informes()
        except Exception as e:
            print("Error Modo informes", e)
    elif seleccion == 4:
        pass
    


# FUNCION CONSULTAR
def consultar(query):#el parmetro query almacenara la consulta
    conn = sqlite3.connect("elParaiso.db") # conecta con la base de datos
    cursor = conn.cursor() # el cursor "selecionara" los registros que le indiqueca la consulta
    cursor.execute(query) # ejecuta lo que le pasa el parametro query (la consulta)
    datos = cursor.fetchall() # fetchall pasa la infomacion a la variable datos
    conn.close() # cierra la coneccion con la base de datos
    return datos

# FUNCION ESPACIOS DISPONIBLES 
# devuelve cuantos asientos hay para un determinado horario 
#   1 es el horario de las 8:00 am
#   2 es el horario de las 10:00 am
#   3 es el horario de las 12:00 md
#   4 es el horario de las 2:00 pm
def espacios_disponibles(numero_de_horario):
    q = f"SELECT COUNT(asiento) FROM reservas WHERE horario = {numero_de_horario}"
    #q cuenta los asientos de un horario dado
    t = 18 #numero total de espacios por horario 6 pasajeros 3 telefericos 18
    o = consultar(q)[0][0] #asientos ocupados
    return t-o #total menos ocupados da los disponibles

def reservas():
    print(separator())
    print ("El teleferico ofrece 4 horarios para que usted pueda disfrutar\nde los recorridos en zonas de las montañas. \n\nEstos son los horarios:\n")
    espacios_8am = espacios_disponibles(1)
    espacios_10am = espacios_disponibles(2)
    espacios_12md = espacios_disponibles(3)
    espacios_2pm = espacios_disponibles(4)


    print ("\t[1] 8:00 am\t",espacios_8am, "espacios disponibles") 
    print ("\t[2] 10:00 am\t",espacios_10am, "espacios disponibles") 
    print ("\t[3] 12:00 md\t",espacios_12md, "espacios disponibles") 
    print ("\t[4] 2:00 pm\t",espacios_2pm, "espacios disponibles") 
    print("\n",separator())
    
    horario = input("Ingrese la opcion con el horario deseado: ")
    print(separator())
    numPersonas = abs(int(input("Cúantas personas harán el Tour?: ")))
    print(separator())

    if (horario == "1" and numPersonas > espacios_8am  
    or horario == "2" and numPersonas > espacios_10am
    or horario == "3" and numPersonas > espacios_12md
    or horario == "4" and numPersonas > espacios_2pm):
        print("No hay espacios disponibles, seleccione otro horario")
        a = input("Presione cualquier tecla para volver al menu: ")
        return menu_de_seleccion()

    else:
        nueva_reservacion(numPersonas, horario)

# la funcion asientos devuelve el numero de asientos de un teleferico n en un horario h
def asientos(n, h):
    # cuenta cuantas veces aparece un registro en la tabla reservas de un teleferico n
    q=f"SELECT COUNT(teleferico) FROM reservas WHERE teleferico = {n} AND horario = {h}"
    return consultar(q)[0][0] #ej de la respuesta sin el [0][0] >>>[(6,)]

def ultima_reservacion():
    q = f"SELECT DISTINCT num_reservacion FROM reservas ORDER BY num_reservacion DESC LIMIT 2"
    x = consultar(q)
    if x:
        return x[0][0]
    else:
        return 0

def nueva_reservacion(personitas, horario):
    try:
        num_reservacion=ultima_reservacion()+1
        print("Numero de Resevacion", num_reservacion)
        if personitas <= 6-asientos(1, horario):
            for i in range(personitas):
                registro(1, num_reservacion, horario, asientos(1, horario)+1)
        elif personitas <= 6-asientos(2, horario):
            for i in range(personitas):
                registro(2, num_reservacion, horario, asientos(2, horario)+1)
        elif personitas <= 6-asientos(3, horario):
            for i in range(personitas):
                registro(3, num_reservacion, horario, asientos(3, horario)+1)
        else:
            while personitas > 0 and asientos(1, horario) < 6:
                registro(1, num_reservacion, horario, asientos(1, horario)+1)
                personitas -=1
            while personitas > 0 and asientos(2, horario) < 6:
                registro(2, num_reservacion, horario, asientos(2, horario)+1)
                personitas -=1
            while personitas > 0 and asientos(3, horario) < 6:
                registro(3, num_reservacion, horario, asientos(3, horario)+1)
                personitas -=1
            
    except Exception as e:
        print(e)

def registro(teleferico, reservacion, horario, asiento):          
            nombre=input("\nDigite un nombre o alias:\n")
            numResrvacion=reservacion
            print("\nhola", nombre, "es?:")
            print("1. Nacional")
            print("2. Extranjero")
            nacionalidad=int(input("\nDigite su selecion:\n"))
            edad=int(input("Digite la edad:"))
            print("-----------------------------------------------------------------------------")
            if 65 > edad > 18 and nacionalidad == 2:
                monto = 7000
            elif 65 > edad > 18 and nacionalidad == 1:
                monto = 5000
            elif nacionalidad == 2:
                monto = 3500
            else:
                monto = 2500
            print("el monto a cancelar para", nombre, "son", monto, "colones")
            print("N° Resevacion",numResrvacion, "Teferico", teleferico, "Asiento",asiento)
            registrar(numResrvacion, nombre, nacionalidad, edad, horario, teleferico, asiento,"22-02-93")
            input("\n\t[ ⏎ ] Enter para volver al menu\n\n")
            menu_de_seleccion()

def registrar(numResvacion, nombre, nacionalidad, edad, horario, teleferico, asiento, fecha):
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"INSERT INTO reservas VALUES (NULL,{numResvacion},'{nombre}',{nacionalidad},{edad},{horario},{teleferico},{asiento},'{fecha}')"
    cursor.execute(query)
    conn.commit()
    conn.close()

def datos_factura(r):
    c=f"SELECT nombre, edad, nacionalidad, num_reservacion FROM reservas WHERE num_reservacion={r}"
    return consultar(c)

def facturacion():
    cliente = input("Ingrese el nombre de la persona a la que se le va a facturar:\n>>> ")
    id_cliente = input("Digite el número de identificación:\n>>> ")
    n_reservacion = int(input("ingrese el numero de reservación:\n>>> " ))
    total=0
    print("""
+--------------------------------------------------------------+
|                     AVENTURAS EL PARAISO                     |
+--------------------------------------------------------------+
    """)
    print("N° Resevacion",n_reservacion)
    codigo_horario = consultar(f"SELECT horario FROM reservas WHERE num_reservacion={n_reservacion}")[0][0]
    if codigo_horario == 1:
        horario = "8am"
    elif codigo_horario == 1:
        horario = "10am"
    elif codigo_horario == 1:
        horario = "12md"
    else:
        horario = "2pm"
    print("Horario:",horario)
    print("Cliente:", cliente)
    print("Id:",id_cliente)
    for r in datos_factura(n_reservacion):
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
        print((nombre)+",",edad,"años\t\t\t", nacionalidad,"\t",monto)
    iva = round(total*0.13)
    print("\t\t\t\tIva\t",iva)
    print("\t\t\t\tTOTAL\t", total+iva)
    input("\n\t[ ⏎ ] Enter para volver al menu\n\n\n")
    menu_de_seleccion()

def personas_horario(h):
    c=f"SELECT COUNT(teleferico) FROM reservas WHERE horario = {h}"
    return consultar(c)

def personas_total():
    c=f"SELECT COUNT(teleferico) FROM reservas"
    return consultar(c)

def contar_tarifa_Adultos(n):
    c=f"SELECT COUNT(teleferico) FROM reservas WHERE nacionalidad={n} AND edad  < 65 AND edad >18"
    return consultar(c)[0][0]

def contar_tarifa_Ninos_Mayores(n):
    c=f"SELECT COUNT(teleferico) FROM reservas WHERE nacionalidad={n} AND edad  > 65 OR nacionalidad={n} AND edad < 18"
    return consultar(c)[0][0]

def horario_mayor():
    c=f"SELECT COUNT(asiento), horario FROM reservas GROUP BY horario ORDER BY COUNT(asiento) DESC LIMIT 1"
    return consultar(c)[0][1]

def horario_menor():
    c=f"SELECT COUNT(asiento), horario FROM reservas GROUP BY horario ORDER BY COUNT(asiento) LIMIT 1"
    return consultar(c)[0][1]

def informes():
    print("[ CANTIDAD TOTAL DE PERSONAS:",personas_total()[0][0],"]")
    h_mayor = horario_mayor()
    if h_mayor==1:
        h="8am"
    elif h_mayor==2:
        h="10am"
    elif h_mayor==3:
        h="12md"
    elif h_mayor==4:
        h="2pm"
    print(f"[ Horoario con mayor cantidad de personas {h} ]")

    h_menor = horario_menor()
    if h_menor==1:
        m="8am"
    elif h_menor==2:
        m="10am"
    elif h_menor==3:
        m="12md"
    elif h_menor==4:
        m="2pm"
    print(f"[ Horoario con menor cantidad de personas {m} ]\n")
    print("[  PERSONAS POR HORARIO Y TELEFERICO  ]")
    print("[8:am ",personas_horario(1)[0][0],"personas]")
    print("  Teleferico 1:",asientos(1,1),"pesonas")
    print("  Teleferico 2:",asientos(2,1),"pesonas")
    print("  Teleferico 3:",asientos(3,1),"pesonas\n")

    print("[8:am ",personas_horario(2)[0][0],"personas]")
    print(" Teleferico 1:",asientos(1,2),"pesonas")
    print(" Teleferico 2:",asientos(2,2),"pesonas")
    print(" Teleferico 3:",asientos(3,2),"pesonas\n")
    
    print("[8:am ",personas_horario(3)[0][0],"personas]")
    print(" Teleferico 1:",asientos(1,3),"pesonas")
    print(" Teleferico 2:",asientos(2,3),"pesonas")
    print(" Teleferico 3:",asientos(3,3),"pesonas\n")

    print("[  DINERO RECAUDADO  ]\n")
    c_adul_nac = contar_tarifa_Adultos(1)
    c_ninosMayores_nac = contar_tarifa_Ninos_Mayores(1)
    c_adul_ext = contar_tarifa_Adultos(2)
    c_ninosMayores_ext = contar_tarifa_Ninos_Mayores(2)

    print("NACIONALES:")    
    print("Adultos ("+str(c_adul_nac)+" personas): ",c_adul_nac*5000)
    print("Niños y Adultos Mayores ("+str(c_ninosMayores_nac)+" personas): ",c_ninosMayores_nac*2500,"\n")

    print("EXTRANGEROS:")    
    print("Adultos ("+str(c_adul_ext)+" personas): ",c_adul_ext*7000)
    print("Niños y Adultos Mayores ("+str(c_ninosMayores_ext)+" personas): ",c_ninosMayores_ext*3500,"\n")

    input("\n\t[ ⏎ ] Enter  para volver al menu.")
    return menu_de_seleccion()



try:
    menu()

except:
    print("Error en menu")