class Nodo():
    def __init__(self, Nombre=None, Tamaño=None, Autor=None, Siguiente = None, S = None):
        self.Nombre  = Nombre
        self.Autor = Autor
        self.Tamaño = Tamaño
        self.Siguiente  = Siguiente
        self.S  = S
      
    def Insertar(self, Nombre, Tamaño, Autor):
        if not self.S == None:
            actual = self.S
            while not actual.Siguiente==None:
                actual=actual.Siguiente
            actual.Siguiente = Nodo(Nombre,Tamaño,Autor)
        else:
            self.S=Nodo(Nombre,Tamaño,Autor)
        
        
class Directorio():
    
    def __init__(self, Nombre=None):
        self.raiz_Nodo = Nodo(Nombre)
        
    def __void(self):
        return self.Primer_Nodo == None
    
    def Insertar(self, Nombre, Tamaño, Autor , ubicacion):
        a=self.buscar(ubicacion)
        a.Insertar(Nombre,Tamaño,Autor)
        
    def buscar(self,Nombre):
        return self.buscar_auxiliar(Nombre,self.raiz_Nodo)
        
    def buscar_auxiliar(self, Nombre, actual):
        while not actual == None:
            if(actual.Nombre==Nombre):
                return actual
            elif not actual.S == None:
                r=self.buscar_auxiliar(Nombre, actual.S) 
                if(r.Nombre == Nombre):
                    return r
            actual == actual.Siguiente
                
        print("File not found")
        
    def cosult(self, dirr, Autor, Tamaño):
        actual = self.buscar(dirr)         
        actual = actual.S
        a= Autor == "any"
        while not actual.Siguiente == None:
            if(a):
                if(actual.Tamaño):
                    print(actual.Nombre)
            else:
                if(actual.Autor == Autor):
                    print(actual.Nombre)
    def imprimir(self):
        actual = self.raiz_Nodo
        print(actual.Nombre)
        actual = actual.S
        while not actual == None:
            print("├──","[",actual.Autor,"",actual.Tamaño,"]",actual.Nombre)
            auxiliar = actual.S
            while not auxiliar == None:
                print("│   └──","[",auxiliar.Autor,"",auxiliar.Tamaño,"]",auxiliar.Nombre)
                auxiliar = auxiliar.Siguiente
            actual = actual.Siguiente