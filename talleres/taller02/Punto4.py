def Subcadena(cadena1, cadena2):
    if(len(cadena1)==0 or len(cadena2)==0):
        return 0
    if(cadena1[len(cadena1)-1] == cadena2[len(cadena2)-1]):
        w = cadena1[:-1]
        z = cadena2[:-1]
        return Subcadena(w, z) + 1
    else:
        x = cadena1[:-1]
        y = cadena2[:-1]
        return max(Subcadena(cadena1, y), Subcadena(x, cadena2))
        
print("La longitud de la subsecuencia común más larga entre las dos cadenas es: " + str(Subcadena("AGGTABZO", "GXTXAYBO")))
