from time import time
import numpy as np
import matplotlib.pyplot as plt

def Fibonacci(n):
    if(n<=1):                               #c_1 = 2           
        return n                            #T(n) = c_1 + c_2         
    return Fibonacci(n-2) + Fibonacci(n-1)  #T(n) = c_3 + T(n-1) + T(n-2)
                                            #T(n) = -c_3 + c_1 Fn + c_2 Ln  
                                            #Donde Fn= es el n número de Fibonacci Y ln = es el n número de Lucas            
for n in range(0,36):
    T1 = time()
    Fibonacci(n)
    T2 = time()
    print(T2-T1)
    plt.plot(n, T2-T1, 'r.')
    
def exponencial(k):
    return (5*(9.8**-7))*(np.e**(0.4618*k))#Exponencial de tendencia

z=np.linspace(0,35,30)
plt.plot(z,exponencial(z), label=r'$5(9.8^{-7})e^{0.4618n}$', color='c') #Gráfica exponencial de tendencia

plt.legend(loc=2)    
plt.title('Complejidad T(n) Fibonacci')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo ejecución (segundos)')  
plt.grid(True)
  
plt.show()
