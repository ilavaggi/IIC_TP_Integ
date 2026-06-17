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
#modulo DiaYHoraMasVentoso
def DiaYHoraMasVentoso(MV):
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
