def Formas_llenado(n):
  if(n <= 2):
    return n
  return Formas_llenado(n-1) + Formas_llenado(n-2)

A = int(input("Ingresa la altura/base del rectángulo"))
print("La cantidad de formas que se puede rellenar un rectángulo de 2x" + str(A) + " con rectángulos de 1x2 es: " + str(Formas_llenado(A)))
