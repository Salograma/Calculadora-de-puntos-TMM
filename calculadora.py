#ARCHIVO EJECUTABLE EN UNA TERMINAL CON UN INTÉRPRETE DE PYTHON
#SOLO SIRVE COMO CÓDIGO FUENTE, NO TIENE NINGUNA INTERFAZ GRÁFICA AÚN, (ME GUSTARÍA AÑADIRLA EN UN FUTURO)

import time
import os

mejores = []

def clear():
    if os.name == "nt":
        os.system('cls')

james_potter = [""] * 10
for i in range(10):
    james_potter[i] = [0] * 5

for i in range(10):
    for j in range(1,4):
        james_potter[i][j] = 0

#Retos diarios: [i][1]
#Rompecabezas o sopas de letras: [i][2]
#Actividades extras: [i][3] (Ingreso manual)
#Galeones: [i][4]

james_potter[0][0] = "Nombre"
james_potter[1][0] = "Nombre1"
james_potter[2][0] = "Nombre2"
james_potter[3][0] = "Nombre3"
james_potter[4][0] = "Nombre4"
james_potter[5][0] = "Nombre5"
#COMO LA MATRIZ TIENE DIEZ POSICIONES SE PUEDEN AGREGAR TRES NOMBRES MÁS COMO ÍNDICES DEL PROGRAMA. POR AHORA FUNCIONA CON 6 ÍNDICES.


def linea(caracter, longitud):
    print(caracter * longitud)

def fecha():
    global dia
    dia = input("Ingrese la fecha de hoy en este formato: DD-MM-AAAA\n")

def cuenta(actividad, columna, puntos):
    for i in range(0,len(james_potter)-1):
        if james_potter[i][0] not in ["", 0]:
            for j in range(30):
                time.sleep(0.01)
                linea("-", j)
                if j != 29:
                    clear()
            opc = "c"
            for j in range(30):
                linea("-",29)
                print(f"¿{james_potter[i][0]} hizo el {actividad} hoy?")
                time.sleep(0.01)
                linea("-", j)
                if j != 29:
                    clear()
            while opc not in ["a", "b"]:
                opc = input("¿Qué opción elige? \na. Sí\nb. No\nSu opción:")
                if opc not in ["a", "b"]:
                    print("Ingreso inválido")
        if opc == "a" and james_potter[i][0] != 0:
            cantidad = 1000
            while (cantidad > 5 or cantidad <= 0) and actividad != "reto diario":
                cantidad = int(input("¿Cuántos?"))
                if cantidad > 5 or cantidad <= 0:
                    print("Ingrese un número válido. Como mínimo 1, como máximo 5.")
            if cantidad != 1000:
                print(f"{james_potter[i][0]} hizo el {actividad}. Se acreditarán {puntos * cantidad} puntos")
            else: 
                print(f"{james_potter[i][0]} hizo el {actividad}. Se acreditarán {puntos} puntos")
            if actividad != "reto diario":
                james_potter[i][columna] += puntos * cantidad
            else:
                james_potter[i][columna] += puntos
            time.sleep(1)
            clear()
        elif opc == "b" and james_potter[i][0] != 0:
            print(f"{james_potter[i][0]} ponete las pilas!")
            time.sleep(0.5)
            clear()

def actividades_extras():
    print("¿Hubo actividades extras hoy?")
    opc = input("¿Qué opción elige? \na. Sí\nb. No\nSu opción:")
    while opc != "a" and opc != "b":
        print("Ingreso inválido.")
        opc = input("Ingrese una opción válida: ")
    if opc == "a":
        for i in range(0,len(james_potter)-1):
            if james_potter[i][0] not in ["", 0]:
                for j in range(30):
                    time.sleep(0.01)
                    linea("-", j)
                    clear()
                if j != 29:
                    clear()
                opc = "c"
                for j in range(30):
                    linea("-",29)
                    print(f"¿{james_potter[i][0]} hizo alguna actividad extra hoy?")
                    time.sleep(0.01)
                    linea("-", j)
                    if j != 29:
                        clear()
                while opc not in ["a", "b"]:
                    opc = input("¿Qué opción elige? \na. Sí\nb. No\nSu opción:")
                    if opc not in ["a", "b"]:
                        print("Ingreso inválido")
                if opc == "a" and james_potter[i][0] != 0:
                    puntos = 100000
                    while puntos > 50000 or puntos < 100:
                        puntos = int(input("¿Pór cuántos puntos fue o fueron la/s actividad/es?"))
                        if puntos > 50000 or puntos < 100:
                            print("Ingreso inválido. Tiene que poner un número entre 100 y 50 000")
                    actividades = 10
                    while actividades >= 10 and actividades <= 0:
                        actividades = input("¿Esos puntos los obtuvo en cuántas actividades? \Ingrese un número entero: ")
                        if actividades >= 10 and actividades < 0:
                            print("Ingrese una cantidad válida, mayor a 0 y menor que 10.")
                    clear()
                    print(f"{james_potter[i][0]} hizo {actividades} actividades aportando un total de {puntos} puntos.")
                    print(f"Promediaste un total de {puntos/actividades} puntos por actividad extra. Felicitaciones.")
                    james_potter[i][3] += puntos
                    time.sleep(1)
                elif opc == "b" and james_potter[i][0] != 0:
                    print(f"{james_potter[i][0]} ponete las pilas!")
                    time.sleep(0.5)
                    clear()
    else:
        print("A otra cosa mariposa. A mandar más actividades!")
        time.sleep(0.5)
        clear()

def galeones():
    print("¿Hoy alguien aportó galeones?")
    aportaron = input("Ingrese si aportaron galeones. \na- Sí. \nb- No\nSu opción: ")
    while aportaron not in ["a", "b"]:
        aportaron = input("Ingrese una opción válida \nSu opción: ")
    if aportaron == "a":
        for i in range(0,len(james_potter)-1):
            if james_potter[i][0] not in ["", 0]:
                for j in range(30):
                    time.sleep(0.01)
                    linea("$", j)
                    if j != 29:
                        clear()
                opc = "c"
                for j in range(30):
                    linea("$",29)
                    print(f"¿{james_potter[i][0]} aportó galeones hoy?")
                    time.sleep(0.01)
                    linea("$", j)
                    if j != 29:
                        clear()
                while opc not in ["a", "b"]:
                    opc = input("¿Qué opción elige? \na. Sí\nb. No\nSu opción:")
                    if opc not in ["a", "b"]:
                        print("Ingreso inválido")
                if opc == "a" and james_potter[i][0] != 0:
                    galeones = int(input(f"¿Cuántos galeones aportó {james_potter[i][0]}?"))
                    while galeones > 20000 and galeones < 0:
                        galeones = int(input("Ingrese una cantidad válida entre 1 y 20000"))
                    print(f"{james_potter[i][0]} aportó {galeones} galeones, lo que le sumará un total de {galeones * 10} puntos.")
                    james_potter[i][4] += galeones * 10
                    time.sleep(1)
                elif opc == "b" and james_potter[i][0] != 0:
                    print(f"{james_potter[i][0]} ponete las pilas!")
                    time.sleep(0.5)
                    clear()
    else:
        print("Pónganse las pilas chicos!")
        time.sleep(0.5)
        clear()

def resultado():
    print(f"Resumen del día {dia}:")
    for i in range(0,len(james_potter)-1):
        if james_potter[i][0] not in ["", 0]:
            total = 0
            for j in range(1,5):
                total += james_potter[i][j]
        print(f"El total de puntos que obtuvo {james_potter[i][0]} hoy es de {total} puntos.")
        mejores.append([total, i])

def casillas_vacias():
    for i in range(0,len(james_potter)-2):
        if james_potter[i][0] == 0:
            james_potter.pop(i)

def ordenamiento():
    for i in range(0,len(mejores)-2):
        for j in range(i+1, len(mejores)-1):
            if mejores[i][0] < mejores[j][0]:
                for k in [0, 1]:
                    aux = mejores[j][k]
                    mejores[j][k] = mejores[i][k]
                    mejores[i][k] = aux

def lista_mejores():
    for i in range(0,len(mejores)-1):
        cornudo = mejores[i][1]
        cornudo = james_potter[cornudo][0]
        print(f"{cornudo} obtiene el {i}º lugar con {mejores[i][0]} puntos")
                    
clear()
casillas_vacias()
print("Tenga cuidado. Deberá hacer un ingreso manual correcto de todos los datos porque no se puede volver hacia atrás.")
time.sleep(0.5)
clear()
fecha()
cuenta("reto diario", 1, 7000)
cuenta("rompecabezas o la sopa de letras", 2, 2000)
actividades_extras()
galeones()
resultado()
ordenamiento()
lista_mejores()
