import sys
sys.setrecursionlimit(5000)
from time import time

#No considero vertical, SOLO horizontal y diagonales
def Verificar_Queens(n, tablero):
    for i in range(n**2):
        if(tablero[i] == '*'):
            #Horizontal
            for j in range(i+1,(int(i/n)+1)*n):
                if(tablero[j]=='*'):
                    return False  
            #Diagonal abajo derecha   #fila  abajo   X    columna derecha
            for l in range(1, min(int((n**2-(i+1))/n) , (((int(i/n)+1)*n)-i-1)) + 1): 
                if(tablero[i+((n*l)+1)+(l-1)] == '*'):
                   return False  
            #Diagonal arriba derecha  #fila arriba  X  columna derecga
            for k in range(1, min(int(i/n) , (((int(i/n)+1)*n)-i-1)) + 1 ): 
                if(tablero[(i-(n*k))+k] == '*'):
                    return False              
    return True

def LLamar_Queens(n):
    Tablero = [0]*(n**2)
    return N_Queens(0, n, Tablero)
    
contador=0

#Función para las posibles soluciones de N-queens
def N_Queens(fila, n, Tablero):   
    for i in range(n):
            
             if(i>0 and fila < n-1):
                for p in range(n):
                    if(Tablero[(fila+1)+p*n] == '*'):
                       for l in range(len(Tablero)):
                           if(l%n > fila):
                               Tablero[l]=0
                       break
            
            Tablero[fila+(i*n)] = '*'
            
            if(Tablero[(n**2)-n] == '*' and Tablero[((n**2)+1)-2*n] == '*'):
                break
            
            if(i>0 and Tablero[fila+((i-1)*n)]=='*'):
                Tablero[fila+((i-1)*n)] = 0
                    
            if(Verificar_Queens(n, Tablero)==True):
                if(fila==n-1):
                    global contador
                    contador += 1  
                else:
                    N_Queens(fila+1, n, Tablero)    
            else:
                Tablero[fila+(i*n)] = 0
    #return N_Queens(0, n, [0]*(n**2))      
    return contador
    
T1=time()           
print(LLamar_Queens(10))
T2=time()
print(T2-T1)
