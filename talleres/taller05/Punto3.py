from time import time
import matplotlib.pyplot as plt

def  Tablas_D_Multiplicar(n):
    for i in range(1,n+1):                                       #T1(n) = c1*n 
        print("\n" + "Tabla de multiplicar del " + str(i))
        for  j in range(1,11):                                  #T2(n) = (c2*10)*n
            print(str(i) + " X " + str(j) + ' = ' + str(i*j))   #T3(n) =c3*10*n

for n in range(300,321):
    T1 = time()
    Tablas_D_Multiplicar(n)
    T2 = time()
    print(T2-T1)
    plt.plot(n, T2-T1, 'go')
    
plt.title('Complejidad T(n) tablas de multiplicar')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo ejecución (segundos)')  
plt.grid(True)
  
plt.show()