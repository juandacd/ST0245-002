from time import time
import matplotlib.pyplot as plt

def OrdenInsert(Lista):
    for A in range(len(Lista)):     #T1(n) = c1*n + c2
        for B in range(A):          #T2(n) = c4*{[n*(n+1)]/2} + c5*n
            if Lista[A]<Lista[B]:   
                Auxilio=Lista[A]
                Lista[A]=Lista[B]
                Lista[B]=Auxilio
    return Lista
    #T(n) = c1*n + c2 + (c4*n^2+c4*n)/2 + c5*n
    #T(n) es O(n^2)
    
def Generar_lista(n):
    lista = [0]*n
    for i in range(n):
        lista[i] = n-i
    return lista
 
for n in range(2777,2798):
    Nums = Generar_lista(n)
    T1 = time()
    OrdenInsert(Nums)
    T2 = time()
    print(T2-T1)
    plt.plot(n, T2-T1, 'go')
    
plt.title('Complejidad T(n)')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo ejecución (segundos)')  
plt.grid(True)
  
plt.show()