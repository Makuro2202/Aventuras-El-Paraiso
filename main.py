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

#la funcion espacios ocupados cuenta cuantas entradas hay en cada horario 
# 1 es el horario de las 8:00 am
# 2 es el horario de las 10:00 am
# 3 es el horario de las 12:00 md
# 4 es el horario de las 2:00 pm
def espacios_ocupados(num_horario):
    conn = sqlite3.connect("elParaiso.db")
    cursor = conn.cursor()
    query = f"SELECT COUNT(num_reservacion) FROM reservas WHERE horario = {num_horario}"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos[0][0]


def reservas():
    print(separator())
    print ("El teleferico ofrece 4 horarios para que usted pueda disfrutar\nde los recorridos en zonas de las montañas. \n\nEstos son los horarios:\n")
    #En el futuro se determinan los espacios por medio de base de datos
    espacios_8am = 18-int(espacios_ocupados(1))
    espacios_10am = 18-int(espacios_ocupados(2))
    espacios_12md = 18-int(espacios_ocupados(3))
    espacios_2pm = 18-int(espacios_ocupados(4))


    print ("\t[1] 8:00 am\t",espacios_8am, "espacios disponibles") 
    print ("\t[2] 10:00 am\t",espacios_10am, "espacios disponibles") 
    print ("\t[3] 12:00 md\t",espacios_12md, "espacios disponibles") 
    print ("\t[4] 2:00 pm\t",espacios_2pm, "espacios disponibles") 
    print("\n",separator())
    
    horario = input("Ingrese la opcion con el horario deseado: ")
    print(separator())
    numPersonas = int(input("Cúantas personas harán el Tour?: "))
    print(separator())


    if horario == "1" and numPersonas > espacios_8am:
        print("No hay espacios disponibles, seleccione otro horario")
        a = input("Presione cualquier tecla para volver al menu: ")
        return menu_de_seleccion()

    elif horario == "1":
        return  nueva_reservacion(numPersonas, espacios_8am)

    elif horario == "2" and numPersonas > espacios_10am:
        print("No hay espacios disponibles, seleccione otro horario")
        a = input("Presione cualquier tecla para volver al menu: ")
        return menu_de_seleccion()
    
    elif horario == "2":
        return nueva_reservacion(numPersonas, espacios_10am)

    elif horario == "3" and numPersonas > espacios_12md:
        print("No hay espacios disponibles, seleccione otro horario")
        a = input("Presione cualquier tecla para volver al menu: ")
        return menu_de_seleccion()
    
    elif horario == "3":
        return nueva_reservacion(numPersonas, espacios_12md)

    elif horario == "4" and numPersonas > espacios_2pm:
        print("No hay espacios disponibles, seleccione otro horario")
        a = input("Presione cualquier tecla para volver al menu: ")
        return menu_de_seleccion()
    
    elif horario == "4":
        return nueva_reservacion(numPersonas, espacios_2pm)


def nueva_reservacion(personitas, espacios):
    try:
        n_Asiento = ["Teleferico 1 Asiento 1","Teleferico 1 Asiento 2","Teleferico 1 Asiento 3","Teleferico 1 Asiento 4","Teleferico 1 Asiento 5","Teleferico 1 Asiento 6","Teleferico 2 Asiento 1","Teleferico 2 Asiento 2","Teleferico 2 Asiento 3","Teleferico 2 Asiento 4","Teleferico 2 Asiento 5","Teleferico 2 Asiento 6","Teleferico 3 Asiento 1","Teleferico 3 Asiento 2","Teleferico 3 Asiento 3","Teleferico 3 Asiento 4","Teleferico 3 Asiento 5","Teleferico 3 Asiento 6"]
        asiento = 18-espacios
        persona = []
        n = 1
        total = 0 
        while personitas > 0:          
            nombre=input("\nDigite el {}° nombre:\n".format(n))
            n += 1
            numResrvacion=1
            print("\nhola", nombre, "es?:")
            print("1. Nacional")
            print("2. Extranjero")
            nacionalidad=int(input("\nDigite su selecion:\n"))
            edad=int(input("Digite la edad:"))
            print(separator())

            if 65 > edad > 18 and nacionalidad == 2:
                print("el monto a cancelar para", nombre, "son 7000 colones, ", n_Asiento[asiento])
                asiento += 1
                total = total+7000
            elif 65 > edad > 18 and nacionalidad == 1:
                print("el monto a cancelar para", nombre, "son 5000 colones", n_Asiento[asiento])
                asiento += 1
                total = total+5000
            elif nacionalidad == 2:
                print("el monto a cancelar para", nombre, "son 3500 colones", n_Asiento[asiento])
                asiento += 1
                total = total+3500
            else:
                print("el monto a cancelar para", nombre, "son 2500 colones", n_Asiento[asiento])
                asiento += 1
                total = total+2500
            personitas -= 1 
        print("\n", separator())
        print("El tatal a cancelar por todo el grupo son", total, "colones", "n° de resevacion #", numResrvacion)
        print("-----------------------------------------------------------------------------")
        persona.append((nombre, edad, nacionalidad, 0, 0))       
        #print(persona)
        #El print es para saber que se guardo la informacion
        a = input("Presione cualquier tecla para volver al menu: ")
        return menu_de_seleccion()
    except Exception as x:
        print(x)
try:
    menu()
except:
    print("Error en menu")