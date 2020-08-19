from time import time

def Suma_grupo(start, nums, target):
    if (start == len(nums)):        #c1
        return target == 0          #T(n) = c1 + c2
    else:
        return Suma_grupo(start+1, nums, target-nums[start]) or Suma_grupo(start+1, nums, target) #T(n) = c3 + 2*T(n-1)
        #T(n) = c1*2^(n-1) + c3*(2^n-1)
        
for n in range(15,26):
    Tiempo_inicial = time()
    Suma_grupo(0, [0]*n, 10)
    Tiempo_final = time()
    print(Tiemp_inicial - Tiempo_final)
