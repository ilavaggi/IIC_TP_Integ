# para usar algunos delay entre opciones
import time

# 3 columnas, 30 filas. Resuelto por comprensión de listas 
MP = [[-1 for _ in range(3)] for _ in range(30)]
MV = [[-1 for _ in range(3)] for _ in range(30)]
MT = [[-1 for _ in range(3)] for _ in range(30)]

iMP = 0
iMV = 0
iMT = 0
jMP = 0
jMV = 0
jMT = 0

Opcion = ""

# para representar mas cómodo las horas en lugar de numeritos, y los nombres de las matruces
hora = {0:"06:00 hs",1:"18:00 hs",2:"22:00 hs"}
mat = {1:"Temperatura",2:"Velocidad de viento",3:"Precipitación"}

# Submenú para seleccionar el dato a cargar
def CargarDatos():
    OPT = ""
    while OPT == "":
        OPT = int(input("""
    Seleccione el dato a cargar:
    1 - Temperatura
    2 - Velocidad de viento
    3 - Precipitación\n"""))
        if OPT == 1:
            MT,iMT,jMT = CargarMatriz(MT,iMT,jMT,0,30, OPT) # Envío el parametro OPT para imprimir un textito que diga qué matriz es
        elif OPT == 2:
            MV,iMV,jMV = CargarMatriz(MV,iMV,jMV,0,15, OPT)
        elif OPT == 3:
            MP,iMP,jMP = CargarMatriz(MP,iMP,jMP,5,10, OPT)
        else:
            print("\nOpción inválida\n")
            OPT = ""
    
# Modulito para cargar la matriz seleccionada en el menú anterior
def CargarMatriz(Matriz, indiceFil, indiceCol, limMin, limMax, OPT):
    if indiceFil > 29:
        print("Datos completamente cargados")
    else:
        print(f"""
        CARGAR NUEVO DATO: {mat[OPT]}
        DIA: {indiceFil+1}
        HORA: {hora[indiceCol]}
        Valor: {"N/D" if Matriz[indiceFil][indiceCol] == -1 else Matriz[indiceFil][indiceCol]}
        Ingrese valor: """)

        VAL = ValidarDato(limMin,limMax)

        conf=""
        while conf == "":
            conf = int(input(f"Usted ingresó {VAL} Confirmar? 1: SI, 2:NO: "))
            if conf == 1:
                Matriz[indiceFil][indiceCol] = VAL
                print(f"""
                ---------- VALOR CARGADO -------------
                    DIA: {indiceFil+1}
                    HORA: {hora[indiceCol]}
                    {mat[OPT]}: {Matriz[indiceFil][indiceCol]}
                --------------------------------------""")           
                indiceCol += 1
                if indiceCol > 2:
                    indiceCol = 0
                    indiceFil +=1
            elif conf == 2:
                    print("Cancelado")
            else:
                print("\nOpción inválida")
                conf=""
    return(Matriz,indiceFil,indiceCol)

# Submódulo para verificar si el dato solicitado está dentro de los rangos permitidos
def ValidarDato(limMin,limMax):
    Valor  = ""
    while Valor == "":
        Valor = int(input(""))
        if Valor > limMin:
            if Valor < limMax:
                return(Valor)
            else:
                print("\nValor fuera de rango. Reingrese.")
                Valor = ""
        else:
            print("\nValor fuera de rango. Reingrese.")
            Valor = ""


#modulo DiaYHoraMasVentoso
def DiaYHoraMasVentoso():
    max_viento = -2
    dia_max = -2
    hora_max = ""
    
    for i in range(30):
        for j in range(3):
            if MV[i][j] == -1:
                # Si max_viento sigue en -1, la matriz estaba vacía
                if max_viento == -1:
                    print("No hay datos cargados")
                else:
                    print(f"Día más ventoso: {dia_max}")
                    print(f"Hora: {hora_max}")
                # Con return para terminar 
                return 
            
            # voy cambiando y me quedo con la velocidad máxima guardada
            if MV[i][j] > max_viento:
                max_viento = MV[i][j]  # Guardamos esta nueva velocidad como la máxima
                dia_max = i + 1        # Guardamos el día real (sumamos 1 porque el índice 'i' empieza en 0)
                
                # acá entiendo que es para designar la hora
                if j == 0:
                    hora_max = "06:00hs"
                elif j == 1:
                    hora_max = "18:00hs"
                else:
                    hora_max = "22:00hs"
                    
    # Este bloque final me sirve para cuando la matriz está full
    if max_viento == -1:
        print("No hay datos cargados")
    else:
        print(f"Día más ventoso: {dia_max}")
        print(f"Hora: {hora_max}")

# SUBMODULO: Promedio de Sensores

def promedioSensores():
    promedio(MT, "temperatura")
    promedio(MP, "precipitacion")
    promedio(MV, "velocidad del viento")
    pass

# SUBMODULO: Promedio(matrizDatos, matrizNombre)
def promedio(matrizDatos, matrizNombre):
    if matrizDatos[0][0] == -1:
        print("Sin datos cargados")
        return
    i = 0
    sumaValores = 0
    cantidad = 0
    while i < 30:
        j = 0
        while j < 3:
            if matrizDatos[i][j] != -1:
                sumaValores = sumaValores + matrizDatos[i][j]
                cantidad = cantidad + 1
            j = j + 1
        i = i + 1

    promedio = sumaValores / cantidad
    print(f"El promedio de {matrizNombre} es: {promedio}")

# SUBMODULO: Día y hora menos lluvioso:
def DiaHoraMenosLluvioso():
    if MP[0][0] == -1:
        print("Sin datos cargados")
        return

    i = 0
    minimo = MP[0][0]
    horaMinimo = 0
    horaString = ""
    diaMinimo = 0

    while i < 30:
        j = 0
        while j < 3:
            if MP[i][j] != -1:
                if minimo > MP[i][j]:
                    minimo = MP[i][j]
                    horaMinimo = j  
                    diaMinimo = i
                j = j + 1
            else:
                break # salir del while de j   
        i = i + 1

    if horaMinimo == 0:
        horaString = "6:00 hs"
    elif horaMinimo == 1:
        horaString = "18 hs"
    elif horaMinimo == 2:
        horaString = "22 hs"
    else: 
        print("Error de cálculo")

    print(f"Día de menor precipitación: {diaMinimo + 1}. Hora de menor precipitación: {horaString}")        




### PROGRAMA / LOOP PRINCIPAL

while Opcion != "000":
    Opcion = input("""Elija una opción:
1 - Ingresar datos de sensores
2 - Mostrar promedio mensual de sensores
3 - Mostrar temperatura maxima y minima del mes
4 - Día y hora mas ventoso del mes
5 - Día y hora menos lluvioso
000 - Para finalizar el programa\n
""")
    if Opcion == "1":
        print(CargarDatos())
    elif Opcion == "2":
        print("Opcion 2 seleccionada")
    elif Opcion == "3":
        print("Opcion 3 seleccionada")
    elif Opcion == "4":
        print("Opcion 4 seleccionada")
    elif Opcion == "5":
        print("Opcion 5 seleccionada")
    elif Opcion == "000":
        print("\nSalimo'\n")
        for i in MP:
            print(i)
        continue # sale del programa en el siguiente chequeo
    else:
        print("\nOpción inválida\n") #las \n son para darle el salto de linea y que no quede todo  re pegado
        time.sleep(1) #esperamos un segundito para que se note que es opcion invalida en el menu
                
