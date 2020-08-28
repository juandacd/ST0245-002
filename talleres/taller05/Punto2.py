from time import time
import matplotlib.pyplot as plt


def Sumar(lista):
    Sumacumulada = 0        # c1 
    for s in lista:         # c2 + c3n
        Sumacumulada += s   # c4n
    return Sumacumulada      # c5
     # T(n) = c1 + c2 + c5 + (c3 + c4)n
     #T(n) es O(n)

for n in range(1000000, 10000000, 1000000):
    T1 = time()
    Sumar([0]*n)
    T2 = time()
    print(T2-T1)
    plt.plot(n, T2-T1, 'go')

plt.title('Complejidad T(n)')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo ejecución (segundos)')  
plt.grid(True)
  
plt.show()