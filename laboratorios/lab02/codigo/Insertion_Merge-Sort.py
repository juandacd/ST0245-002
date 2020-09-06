import matplotlib.pyplot as plt
import numpy as np
from time import time

def OrdenInsert(Lista):
    for y in range(1, len(Lista)): 
        A = Lista[y]
        g = y-1
        while g >=0 and A < Lista[g]:
            Lista[g+1] = Lista[g]
            g -= 1
        Lista[g+1] = A
    return Lista
  
     
def MergeSort(Lista):
    if len(Lista) >1: 
        m = len(Lista)//2 
        izquierda = Lista[:m] 
        derecha = Lista[m:] 
  
        MergeSort(izquierda) 
        MergeSort(derecha) 
  
        i = 0
        j = 0
        k = 0
          
        while i < len(izquierda) and j < len(derecha): 
            if izquierda[i] < derecha[j]: 
                Lista[k] = izquierda[i] 
                i+=1
            else: 
                Lista[k] = derecha[j] 
                j+=1
            k+=1
          
        while i < len(izquierda): 
            Lista[k] = izquierda[i] 
            i+=1
            k+=1
          
        while j < len(derecha): 
            Lista[k] = derecha[j] 
            j+=1
            k+=1
    return Lista
     
       
def Generar_lista(n):
    lista = [0]*n
    for i in range(n):
        lista[i] = n-i
    return lista


for n in range(3000, 3020):
    Nums = Generar_lista(n)
    T1 = time()
    OrdenInsert(Nums)
    T2 = time()
    print(T2-T1)
    colors = ("blue")
    area = np.pi*2
    plt.scatter(n, T2-T1, s=area, c=colors, alpha=1)
    
    
for n in range(3000, 3020):
    Nums = Generar_lista(n)
    T1 = time()
    MergeSort(Nums)
    T2 = time()
    print(T2-T1)
    colors = ("green")
    area = np.pi*2
    plt.scatter(n, T2-T1, s=area, c=colors, alpha=1)

plt.show()