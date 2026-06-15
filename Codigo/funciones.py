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