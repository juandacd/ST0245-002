def combinaciones(cadena):
    permutations("",cadena)
    
def permutations(base, cadena):
    if (len(cadena) == 0 ):
        print(base)
    else:
        i = 0
        for i in range (len(cadena)):
            permutations(base + cadena[i], cadena[0:i] + cadena[i+1:len(cadena)])
                    
combinaciones("wxyz")