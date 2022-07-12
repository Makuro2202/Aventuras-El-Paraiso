# PROJECTO FINAL GRUPO 01. UNIVERSIDAD FIDELITAS
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
        except:
            print("Error Modo informes")
    elif seleccion == 4:
        salir()

def informes():
    print(separator())
    a = input("Presione la tecla k para volver al menu: ")
    if a =="k":
        return menu_de_seleccion()
    #
    #Falta este modulo
    #
    return informes()

def facturacion():
    print("""Menu de facturación, seleccione la opción que desea

    \t[1] Nacionales
    \t[2] Extranjeros
    \t[3] Salir
    """)
    print(separator())
    seleccion = int(input("Digite una opcion: "))
    if seleccion == 1:
        try:
            nacionales()
        except:
            pass
    elif seleccion == 2:
        try:
            extranjeros()
        except:
            pass
    elif seleccion == 3:
        try:
            salir()
        except:
            pass

    def nacionales():
        print(separator())
    adultos1 = 5000
    cantidad1 = int(input("Digite la cantidad de Adultos: "))
    niñoadultomayor1 = 2500
    cantidad2 = int(input("Digite la cantidad de niños y adultos mayores: "))
    totaladultos = adultos1*cantidad1
    totalniñosadultomayor = niñoadultomayor1*cantidad2
    iva = 1.13
    print("Monto Subtotal de adultos: ",totaladultos, "Monto subtotal de niños y Adultos Mayores: ",totalniñosadultomayor)
    total = (totalniñosadultomayor+totaladultos)*iva
    redondeo = round(total)
    print("Gran Total: ",redondeo)
    print(separator())
    a = input("Presione la tecla m para volver al menu de facturación: ")
    if a =="m":
        return facturacion()

    def extranjeros():
        print(separator())
        adultos2 = 7000
        cantidad3 = int(input("Digite la cantidad de adultos Extranjeros es: "))
        niñoadultomayor2 = 3500
        cantidad4 = int(input("Digite la cantidad de niños y adultos mayores es: "))
        totaladultos = adultos2*cantidad3
        totalniñosadultomayor = niñoadultomayor2*cantidad4
        iva = 1.13
        print("Monto Subtotal de adultos: ",totaladultos, "Monto subtotal de niños y Adultos Mayores: ",totalniñosadultomayor)
        total = (totalniñosadultomayor+totaladultos)*iva
        redondeo = round(total)
        print("Gran Total: ",redondeo)
        print(separator())
        a = input("Presione la tecla m para volver al menu de facturación: ")
        if a =="m":
            return facturacion()
    
def salir():
    print(separator())
    a = input("Presione la tecla m para volver al menu principal: ")
    if a =="m":
        return menu_de_seleccion()

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

# la funcion asientos devuelve el numero de asientos de un teleferico n
def asientos(n):
    q=f"SELECT COUNT(teleferico) FROM reservas WHERE teleferico={n}"
    # coenta cuantas veces aparece un registro en la tabla reservas de un teleferico n
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
        if personitas <= 6-asientos(1):
            for i in range(personitas):
                registro(1, num_reservacion, horario, asientos(1)+1)
        elif personitas <= 6-asientos(2):
            for i in range(personitas):
                registro(2, num_reservacion, horario, asientos(2)+1)
        elif personitas <= 6-asientos(3):
            for i in range(personitas):
                registro(3, num_reservacion, horario, asientos(3)+1)
        else:
            while personitas > 0 and asientos(1) < 6:
                registro(1, num_reservacion, horario, asientos(1)+1)
                personitas -=1
            while personitas > 0 and asientos(2) < 6:
                registro(2, num_reservacion, horario, asientos(1)+1)
                personitas -=1
            while personitas > 0 and asientos(3) < 6:
                registro(3, num_reservacion, horario, asientos(1)+1)
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

def registrar(numResvacion, nombre, nacionalidad, edad, horario, teleferico, asiento, fecha):
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"INSERT INTO reservas VALUES (NULL,{numResvacion},'{nombre}',{nacionalidad},{edad},{horario},{teleferico},{asiento},'{fecha}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
try:
    menu()
except:
    print("Error en menu")