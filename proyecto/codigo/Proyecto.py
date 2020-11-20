import pandas as pd
import numpy as np

Datos = pd.read_csv('0_train_balanced_15000.csv', sep= ';', header=0)

#Filtro = Datos.dropna(axis=1) #Elimina columnas que tiene valores NaN
Filtro = Datos.iloc[:,[4, 5, 6, 7, 8, 9, 10, 13, 22, 23, 24, 25, 32, 35, 
                       36, 42, 45, 48, 50, 52, 53, 54, 55, 57, 58, 60, 61, 
                       62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77]] #Aspectos que consideramos 

Filtro = Filtro.fillna(0) #Cambia datos NaN(vacíos) por 0
Aspectos = tuple(Filtro.columns.values)

#print(Filtro.dtypes) #Tipo de dato cada item-columna
#print(Filtro.info())#Tipos de datos y uso de la memoria

i=0
for i in range (len(Aspectos)):
    if(Filtro.iloc[:,i].dtype == 'float64'):
        Filtro.iloc[:,i] = Filtro.iloc[:,i].astype('float16')
    if(Filtro.iloc[:,i].dtype == 'int64'):
        Filtro.iloc[:,i] = Filtro.iloc[:,i].astype('int16') # Se cambia el tipo de dato para usar menos memoria
        
print(Filtro.info())#Tipos de datos y uso de la memoria

def Impureza_de_Gini(Filtro):
    
    CantidadEstudiantes = len(Filtro["exito"])
    Exito = len(Filtro[Filtro["exito"] == 1])
    NoExito = len(Filtro[Filtro["exito"] == 0])
    
    Impureza = 1 - (((NoExito/CantidadEstudiantes)**2) - ((Exito/CantidadEstudiantes)**2)) 
    return Impureza
    

def Impureza_de_Gini_Ponderada(FiltroIzquierda, FiltroDerecha):

    Estudiantes1 = len(FiltroDerecha["exito"])
    Estudiantes2 = len(FiltroIzquierda["exito"])
    ImpurezaGiniDerecha = Impureza_de_Gini(FiltroDerecha)
    ImpurezaGiniIzquierda = Impureza_de_Gini(FiltroIzquierda)
    
    ImpurezaGiniPonderada = ((Estudiantes1*ImpurezaGiniDerecha) + (Estudiantes2*ImpurezaGiniIzquierda)) / (Estudiantes1 + Estudiantes2)
    return ImpurezaGiniPonderada


def Shannon(dataFrame):
    CantidadEstudiantes = len(dataFrame["exito"])
    Exito = len(list(Filtro[Filtro["exito"] == 1]["exito"]))
    NoExito = len(list(Filtro[Filtro["exito"] == 0]["exito"]))
    CantidadEstudiantes = len(dataFrame["exito"])
    if (Exito == 0 or NoExito == 0):
        return 0
    shannon = -((Exito/CantidadEstudiantes) * np.log2(Exito/CantidadEstudiantes)) - ((NoExito/CantidadEstudiantes) * np.log2(NoExito/CantidadEstudiantes))
    return shannon


def Ganancia_Información(FiltroPrincipal, FiltroIzquierda, FiltroDercha):
    
    CantidadEstudiantesPrincipal = len(FiltroPrincipal["exito"])
    CantidadEstudiantesIzquierda = len(FiltroIzquierda["exito"])
    CantidadEstudiantesDerecha = len(FiltroDercha["exito"])
    
    ShannonPrincipal = Shannon(FiltroPrincipal)
    ShannonIzquierda = Shannon(FiltroIzquierda)
    ShannonDerecha = Shannon(FiltroDercha)
    Ganacia = ShannonPrincipal - (((CantidadEstudiantesIzquierda /  CantidadEstudiantesPrincipal) *  ShannonIzquierda) +
                              ((CantidadEstudiantesDerecha / CantidadEstudiantesPrincipal) * ShannonDerecha))
    return Ganacia


class Nodo():
 
    def __init__(self, aspecto, limit, Condición):
        self.aspecto = aspecto
        self.limit = limit
        self.Condición = Condición
        self.NodoDerecho = None
        self.NodoIzquierdo = None    
        self.Resultado = ""
        

def Valores_Aspecto(Aspecto): #Valores que puede contener un aspecto   
    ValoresAspecto = tuple(set(Filtro[Aspecto]))
    return ValoresAspecto
#print(Valores_Aspecto("estu_trabajaactualmente"))
    
def EsUnNúmero(ValoresAspecto): #Verifica si los valores de cierto aspecto son numéricos
    try:
        for a in ValoresAspecto:
            b = int(a)
        return True
    except ValueError as error:
        return False
#print(EsUnNúmero(Valores_Aspecto("cole_jornada")))
#print(EsUnNúmero(Valores_Aspecto("punt_matematicas")))    
def Mejor_Condición_Aspecto(Aspecto, ValoresAspecto):
    if(EsUnNúmero(ValoresAspecto)):
        Ganancia = [-1,-1,-1, ">=", -1] #Ganancia, valorDeLaCondicion, Aspecto, condicion, indice
        Datos = Filtro.sort_values(by=[Aspecto])
        Valores = list(Datos[Aspecto])
        for j in range(len(Valores) - 1):
            if (j != 0 and Valores[j] == Valores[j - 1]):
                continue
            else:
                GananciaTemp = Ganancia_Información(Datos, Datos.iloc[0:j], Datos.iloc[j:])
                if (GananciaTemp > Ganancia[0]):
                    Ganancia[0] = GananciaTemp
                    Ganancia[1] = Valores[j]
                    Ganancia[4] = j
        Ganancia[2] = Aspecto
        return Ganancia
    
    else:
        Ganancia = [-1,0, Aspecto, "=="] #Ganancia, valorDeLaCondicion, Aspecto, condicion
        for i in ValoresAspecto:
            GananciaTemp = Ganancia_Información(Datos, Datos.drop(Datos[Datos[Aspectos] != i].index), Datos.drop(Datos[Datos[Aspectos] == i].index))
            if (GananciaTemp > Ganancia[0]):
                    Ganancia[0] = GananciaTemp
                    Ganancia[1] = i
        return Ganancia
    
    
def Mejor_Condición_Aspectos(Filtro, Aspecto):
    MejorCondiciónCadaAspecto = []
    for Aspecto in Aspectos:
        ValoresAspecto = Valores_Aspecto(Aspecto)
        MejorCondiciónCadaAspecto.append(Mejor_Condición_Aspecto(Filtro, Aspecto, ValoresAspecto))

    GananciaMaxima = [-1,-1, "Materia", "Condición", "índice"]
    for MejorCondición in MejorCondiciónCadaAspecto:
        if (MejorCondición[0] > GananciaMaxima[0]):
            GananciaMaxima = MejorCondición

    ValoresAspecto = Valores_Aspecto(GananciaMaxima[2])
    if (EsUnNúmero(ValoresAspecto)):
        DatosDerecha = Filtro.iloc[0 : GananciaMaxima[4]]
        DatosIzquierda = Filtro.iloc[GananciaMaxima[4]:]
    else:
        GananciaMaxima.append(1)
        DatosIzquierda = Filtro.drop(Filtro[Filtro[Aspecto] != MejorCondición[2]].index)
        DatosDerecha = Filtro.drop(Filtro[Filtro[Aspecto] == MejorCondición[2]].index)
    
    GananciaMaxima.append(DatosIzquierdauierda)
    GananciaMaxima.append(DatosDerecha)
    return GananciaMaxima


def CrearArbol():
    Aspectos = Filtro.colums
    Aspectos = Aspectos.drop("exito")
    MejorDecision = Mejor_Condición_Aspectos(Filtro, Aspectos)

    Arbol = Nodo(MejorDecision[2], MejorDecision[1], MejorDecision[3])

    Aspectos = Aspectos.drop(MejorDecision[2])
    DatosIzquierda = MejorDecision[5]
    DatosDerecha = MejorDecision[6]

    CrearArbolAuxiliar(DatosIzquierda, DatosDerecha, Arbol, Aspectos, "Mitad")
    
    EscribirArbol(Arbol)


def CrearArbolAuxiliar(DatosIzquierda, DatosDerecha, Arbol, Aspectos, Lado): #Recursión
    ShannonIzquierda = Shannon(DatosIzquierda)
    ShannonDerecha = Shannon(DatosDerecha)
    if (ShannonIzquierda == 0 and ShannonDerecha == 0):
        print("Entró")
        if (Lado == "Izquierda"):
            Arbol.prediccion = "return True"
        elif (Lado == "Derecha"):
            Arbol.prediccion = "return False"
    elif(len(Aspectos) < 1):
        print("Entró")
        if (Lado == "Izquierda"):
            Arbol.prediccion = "return True"
        elif (Lado == "Derecha"):
            Arbol.prediccion = "return False"
    elif (ShannonDerecha == 0 and len(DatosIzquierda) >= 100):
        MejorDecision = Mejor_Condición_Aspectos(DatosIzquierda, Aspectos)
        NodoIzquierdo = Nodo(MejorDecision[2], MejorDecision[1], MejorDecision[3])
        DatosIzquierdaTemp = MejorDecision[5]
        DatosDerechaTemp = MejorDecision[6]
        Aspectos = Aspectos.drop(MejorDecision[2])
        CrearArbolAuxiliar(DatosIzquierdaTemp, DatosDerechaTemp, NodoIzquierdo, Aspectos, "Izquierda")
    elif (ShannonIzquierda == 0 and len(DatosDerecha) >= 100):
        MejorDecision = Mejor_Condición_Aspectos(DatosDerecha, Aspectos)
        NodoDerecho = Nodo(MejorDecision[2], MejorDecision[1], MejorDecision[3])
        DatosIzquierdaTemp = MejorDecision[5]
        DatosDerechaTemp = MejorDecision[6]
        Aspectos = Aspectos.drop(MejorDecision[2])
        CrearArbolAuxiliar(DatosIzquierdaTemp, DatosDerechaTemp, NodoDerecho, Aspectos, "Derecha")

    elif (len(DatosIzquierda) >= 100 or len(DatosDerecha) >= 100):
        if (len(DatosIzquierda) >= 100):
            MejorDecision = Mejor_Condición_Aspectos(DatosIzquierda, Aspectos)
            NodoIzquierdo = Nodo(MejorDecision[2], MejorDecision[1], MejorDecision[3])
            DatosIzquierdaPrimero = MejorDecision[5]
            DatosDerechaPrimero = MejorDecision[6]
            Aspectos1 = Aspectos.drop(MejorDecision[2])
            CrearArbolAuxiliar(DatosIzquierdaPrimero, DatosDerechaPrimero, NodoIzquierdo, Aspectos1, "Izquierda")

        if (len(DatosDerecha) >= 100):
            MejorDecision2 = Mejor_Condición_Aspectos(DatosDerecha, Aspectos)
            NodoDerecho = Nodo(MejorDecision2[2], MejorDecision2[1], MejorDecision2[3])
            DatosIzquierdaSegundo = MejorDecision2[5]
            DatosDerechaSegundo = MejorDecision2[6]
            Aspectos2 = Aspectos.drop(MejorDecision2[2])
            CrearArbolAuxiliar(DatosIzquierdaSegundo, DatosDerechaSegundo, NodoDerecho, Aspectos2, "Derecha")

    if (Lado == "Izquierda"):
            Arbol.prediccion = "return True"
    elif (Lado == "Derecha"):
        Arbol.prediccion = "return False"


def EscribirArbol(Arbol):
    archivo = open("Predecir.py", "w")
    archivo.write("def predecir(dataset): \n")
    EscribirArbolAux(Arbol, archivo, "  ")
    archivo.close()


def EscribirArbolAux(Arbol, archivo, espacio):
    if (Nodo.NodoIzquierdo == None and Arbol.NodoDerecho == None):
        archivo.write(espacio + Arbol.prediccion + "\n")
    elif(Arbol.NodoDerecho == None):
        nuevoEspacio = "    " + espacio
        archivo.write(espacio + "if" + " (dataset[[" + "\"" + Arbol.atributo + "\"]]" + Arbol.tipoDeCondicion + str(Arbol.limite)  + "):\n")
        EscribirArbolAux(Arbol.NodoIzquierdo, archivo, nuevoEspacio)
    elif(Arbol.NodoIzquierdo == None):
        nuevoEspacio = "    " + espacio
        archivo.write(espacio + "else: \n")
        EscribirArbolAux(Arbol.NodoDerecho, archivo, nuevoEspacio)
    else:
        nuevoEspacio =  "   " + espacio
        archivo.write(espacio + "if" + " (dataset[[" + "\"" + Arbol.atributo + "\"]]" + Arbol.tipoDeCondicion + str(Arbol.limite)  + "):\n")
        EscribirArbolAux(Arbol.NodoIzquierdo, archivo, nuevoEspacio)

        archivo.write(espacio + "else: \n")
        EscribirArbolAux(Arbol.NodoDerecho, archivo, nuevoEspacio)
