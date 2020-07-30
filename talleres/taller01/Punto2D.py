import math

class Punto2D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def get_x(self):
        return self.x


    def get_y(self):
        return self.y

 
    def radio_polar(self):
        return math.sqrt(self.x**2+self.y**2)

 
    def angulo_polar(self):
        return math.atan2(self.y, self.x)

 
    def dist_euclidiana(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 ) 
    
#print(Punto2D(3.2,5.78).angulo_polar())
        
