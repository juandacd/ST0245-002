from time import time
import matplotlib.pyplot as plt
import numpy as np

def Suma_grupo(start, nums, target):
    if (start == len(nums)):        #c1
        return target == 0          #T(n) = c1 + c2
    else:
        return Suma_grupo(start+1, nums, target-nums[start]) or Suma_grupo(start+1, nums, target) #T(n) = c3 + 2*T(n-1)
        #T(n) = c1*2^(n-1) + c3*(2^n-1)
        
for n in range(10,25):
    T1 = time()
    Suma_grupo(0, [0]*n, 10)
    T2 = time()
    print(T2-T1)
    plt.plot(n, T2-T1, 'go')

def exponencial(k):
    return (6*(9.8**-7.2))*(np.e**(0.712*k)) #Gráfica exponencial de tendencia

z=np.linspace(10,25,20)
plt.plot(z,exponencial(z), label=r'$6(9.8^{-7.2})e^{0.712n}$', color='m') 

plt.legend(loc=2)
plt.title('Complejidad T(n) de groupSum')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo (segundos)')  
plt.grid(True)
  
plt.show()
