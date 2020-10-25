class Abeja():
    
    def __init__(self, latitud, longitud, altitud):
        self.latitud = latitud
        self.lontitud = longitud
        self.altitud = altitud
        
    def getAltitud(self):
        return self.latitud
    
    def getLongitud(self):
        return self.lontitud
    
    def getLatitud(self):
        return self.latitud
    
    def getDistancia(self, Abeja2):
        Distancia = ((self.getAltitud() - Abeja2.getAltitud())**2 +
                     (self.getLongitud() - Abeja2.getLongitud())**2 +
                     (self.getLatitud() - Abeja2.getLatitud())**2)**(1/2)
        return Distancia
    
    
class Nodo():
    
    def __init__(self, AbejaDato, Distancia=0):
        self.AbejaDato = AbejaDato
        self.Distancia = Distancia
        self.Derecho = None
        self.Izquierdo = None
        
    def getDistancia(self):
        return self.Distancia
    
    
class Árbol():
    
    def __init__(self, raiz):
        self.raiz = raiz
        
    def getRaiz(self):
        return self.raiz
    
    def Agregar(self, parámetro, valor, AbejaGuardar):
        if(parámetro == None):
            return
        if(parámetro.Distancia < valor):
            if(parámetro.Derecho != None):
                self.Agregar(parámetro.Derecho, valor, AbejaGuardar)
            else:
                parámetro.Derecho = Nodo(AbejaGuardar, valor)
        else:
            if(parámetro.Izquierdo != None):
                self.Agregar(parámetro.Izquierdo, valor, AbejarGuardar)
            else:
                parámetro.Izquierdo = Nodo(AbejaGuardar, valor)
            
    
class  AbejasÁrbol():
    
    def __init__(self, Abejita):
        self.Abejita = Abejita
        self.AbejaGuardada = Árbol(Nodo(Abejita))
        
    def GuardarAbejas(self, Abejota):
        if(self.Abejita.getDistancia(Abejota) > 100):
            return False
        else:
            self.AbejaGuardada.Agregar(self.AbejaGuardada.getRaiz(), self.Abejita.getDistancia(Abejota), Abejota)
            return True
    
    

Abeja1 = Abeja(3,7,9)
Abeja2 = Abeja(1,9,2)
Abeja3 = Abeja(5,1,4)
Abeja4 = Abeja(5,6,6)
Abeja5 = Abeja(9,2,8)

Árbolito = AbejasÁrbol(Abeja1)
Árbolito.GuardarAbejas(Abeja2)
Árbolito.GuardarAbejas(Abeja3)
Árbolito.GuardarAbejas(Abeja4)
Árbolito.GuardarAbejas(Abeja5)