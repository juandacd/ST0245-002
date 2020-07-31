import math
class Punto2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
   
   
Coordenada1 = Punto2D(5,2)
Coordenada2 = Punto2D(0,12)


class Línea2D():
    
    def __init__(self, Coordenada1, Coordenada2):
        self.Punto1 = Coordenada1
        self.Punto2 = Coordenada2
        
    def get_punto1(self):
        #return "("+str(self.Punto1.get_x())+","+str(self.Punto1.get_y())+")"
        Point = (self.Punto1.get_x(), self.Punto1.get_y())
        return Point
    
    def get_punto2(self):
        #return "("+str(self.Punto2.get_x())+","+str(self.Punto2.get_y())+")"
        Point = (self.Punto2.get_x(), self.Punto2.get_y())
        return Point
        
        
    def Puntos_Intermedios(self):
        Puntos_Intermedios = []
        if((self.Punto1.get_x() - self.Punto2.get_x()) != 0):
            if((self.Punto1.get_y() - self.Punto2.get_y()) != 0):
                Pendiente = (self.Punto1.get_y() - self.Punto2.get_y())/(self.Punto1.get_x() - self.Punto2.get_x())
                if(Pendiente == int(Pendiente)):        
                    Intermedios = abs(self.Punto1.get_x() - self.Punto2.get_x()) - 1
                    if(Intermedios > 0):
                        if(Pendiente > 0):                       
                            if(self.Punto1.get_x() < self.Punto2.get_x()):
                                for i in range(Intermedios):
                                    t=(self.Punto1.get_x()+(i+1), self.Punto1.get_y()+((i+1)*int(Pendiente)))
                                    Puntos_Intermedios.append(t)
                            else:
                                for i in range(Intermedios):
                                    t=(self.Punto2.get_x()+(i+1), self.Punto2.get_y()+((i+1)*int(Pendiente)))
                                    Puntos_Intermedios.append(t)
                        else:
                            if(self.Punto1.get_x() < self.Punto2.get_x()):
                                for i in range(Intermedios):
                                    t=(self.Punto1.get_x()+(i+1), self.Punto1.get_y()+((i+1)*int(Pendiente)))
                                    Puntos_Intermedios.append(t)
                            else:
                                for i in range(Intermedios):
                                    t=(self.Punto2.get_x()+(i+1), self.Punto2.get_y()+((i+1)*int(Pendiente)))
                                    Puntos_Intermedios.append(t)
                    else:
                        return "No hay puntos intermedios"
                else:
                    return "No hay puntos intermedios"
            else:
                Intermedios = abs(self.Punto1.get_x()- self.Punto2.get_x()) - 1
                if(Intermedios > 0):
                    if(self.Punto1.get_x() < self.Punto2.get_x()):
                        for i in range(Intermedios):
                            t=(self.Punto1.get_x()+(i+1), self.Punto1.get_y())
                            Puntos_Intermedios.append(t)
                    else:
                        for i in range(Intermedios):
                            t=(self.Punto2.get_x()+(i+1), self.Punto2.get_y())
                            Puntos_Intermedios.append(t)
                else:
                    return "No hay puntos intermedios"
        else:
            Intermedios = abs(self.Punto1.get_y()- self.Punto2.get_y()) -1 
            if(Intermedios > 0):
                if(self.Punto1.get_y() < self.Punto2.get_y()):
                     for i in range(Intermedios):
                            t=(self.Punto1.get_x(), self.Punto1.get_y()+(i+1))
                            Puntos_Intermedios.append(t)
                else:
                    for i in range(Intermedios):
                            t=(self.Punto2.get_x(), self.Punto2.get_y()+(i+1))
                            Puntos_Intermedios.append(t)
            else:
                return  "No hay puntos intermedios"
        return Puntos_Intermedios
                                
                        
print("Punto1: " + str(Línea2D(Coordenada1, Coordenada2).get_punto1()))
print("Punto2: " + str(Línea2D(Coordenada1, Coordenada2).get_punto2()))
print("Puntos intermedios: " + str(Línea2D(Coordenada1, Coordenada2).Puntos_Intermedios()))
      
