# 3 columnas, 30 filas. Resuelto por comprensión de listas 
MP = [[-1 for _ in range(3)] for _ in range(30)]

iMP = 0
jMP = 0

hora = {0:"06:00 hs",1:"18:00 hs",2:"22:00 hs"}

def CargarMatriz(Matriz, indiceFil, indiceCol):
    if indiceFil > 29:
        print("Datos completamente cargados")
        input("Test")
    else:
        TMP = int(input(f"""
        CARGAR NUEVO DATO:
        DIA: {indiceFil+1}
        HORA: {hora[indiceCol]}
        TEMP: {"N/D" if Matriz[indiceFil][indiceCol] == -1 else Matriz[indiceFil][indiceCol]}
        Ingresar temperatura: """))
        if TMP < 30 and TMP > 0:
            conf = int(input(f"Usted ingresó {TMP} Confirmar? 1: SI, 2:NO:    "))
            if conf != 1 and conf != 2:
                print("Valor Invalido")
            elif conf == 1:
                Matriz[indiceFil][indiceCol] = TMP
                print(f"""
                ---------- VALOR CARGADO -------------
                DIA: {indiceFil+1}
                HORA: {hora[indiceCol]}
                TEMP: {Matriz[indiceFil][indiceCol]}
                --------------------------------------""")           
                indiceCol += 1
                if indiceCol > 2:
                    indiceCol = 0
                    indiceFil +=1
                
            else:
                print("Cancelado")
        else:
            print("Valor invalido. Reingrese.")  

    return(Matriz,indiceFil,indiceCol)

try:
    while True:
        MP,iMP,jMP = CargarMatriz(MP,iMP,jMP)
        

except KeyboardInterrupt:
    print("Salimo'")
    for i in MP:
        print(i)

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
def DiaHoraMenosLluvioso(MP):
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
