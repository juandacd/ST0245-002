import pandas as pd

Datos = pd.read_csv('0_train_balanced_15000.csv', sep= ';', header=0)

#Filtro = Datos.dropna(axis=1) #Elimina columnas que tiene valores NaN
Filtro = Datos.iloc[:,[2, 4, 5, 6, 7, 8, 9, 10, 13, 19, 22, 23, 24, 25, 32, 35, 
                       36, 42, 45, 48, 50, 52, 52, 53, 54, 55, 56, 57, 58, 60, 61, 
                       62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77]] #Aspectos que consideramos 

Filtro = Filtro.fillna(0) #Cambia datos NaN(vacíos) por 0
Aspectos = tuple(Filtro.columns.values)

#print(Filtro.dtypes) #Tipo de dato cada item-columna
print(Filtro.info())

i=0
for i in range (len(Aspectos)):
    if(Filtro.iloc[:,i].dtype == 'float64'):
        Filtro.iloc[:,i] = Filtro.iloc[:,i].astype('float16')
    if(Filtro.iloc[:,i].dtype == 'int64'):
        Filtro.iloc[:,i] = Filtro.iloc[:,i].astype('int16') # Se cambia el tipo de dato para usar menos memoria
        
print(Filtro.info())#Tipos de datos y uso de la memoria
