import random
from time import time
import matplotlib.pyplot as plt

def Maximus(nums, start):
    if((start > len(nums)) or (start < 1)): #c_1 = 4
        return 0;                           #T(n) = c_1 + c_2
    else:
        return max(Maximus(nums,start-1), nums[start-1]); #T(n) = c_3 + T(n-1)
                                                         #T(n) = c_3*n + c_1   

def Generar_lista(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = random.randint(-1000, 1000)
    return lista

for n in range(1,2500):
    T1 = time()
    Maximus(Generar_lista(n), n)
    T2 = time()
    print(T2-T1)
    plt.plot(n, T2-T1, 'b,')
    
plt.axis([0, 2500, 0, 0.02])
plt.title('Complejidad T(n) ArrayMax')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo (segundos)')  
plt.grid(True)
  
plt.show()
