def add(Tabla,s,p):
    Tabla[s]=p
        
def BuscarEmpresa(Tabla,s):
    if(s in Tabla):
        print("La empresa", s,"se encuentra en la lista")
    else:
        print("La empresa", s,"no se encuentra en la lista")
            
def BuscarPais(Tabla,p):
    a = False
    for x in Tabla.values():
        if (p == x):
            a = True
            break
    if(a):
        print("Se tienen empresas en el pais", p)
    else:
        print("No se tienen empresas en el pais", p)
        
Table={}
add(Table,"Google", "Estados Unidos")
add(Table,"La locura", "Colombia")
add(Table,"Nokia", "Finlandia")
add(Table,"Sony", "Japón")
for a, b in Table.items():
    print(a, "\u2192", b)
BuscarEmpresa(Table, "Google")
BuscarEmpresa(Table, "Motorola")
BuscarPais(Table, "Estados Unidos")
BuscarPais(Table, "India")