class Fecha():

    def __init__(self, día, mes, año):
        self.día = día
        self.mes = mes
        self.año = año


    def get_día(self):
        return self.día


    def get_mes(self):
        return self.mes
    
    
    def get_año(self):
        return self.año

    
    def Comparar_Fechas(self, other):
        if(self.año != other.año):
            if(self.año > other.año):
                return "Esta fecha es mayor a la otra"
            else:
                return "Esta fecha es menor a la otra"
        else:
            if(self.mes != other.mes):
                if(self.mes > other.mes):
                    return "Esta fecha es mayor a la otra"
                else:
                    return "Esta fecha es menor a la otra"
            else:
                if(self.día != other.día):
                    if(self.día > other.día):
                        return "Esta fecha es mayor a la otra"
                    else:
                        return "Esta fecha es menor a la otra"
                else:
                    return "Las fechas son iguales"
            
 
    def Mostrar_Fecha(self):
        return str(self.día)+"/"+str(self.mes)+"/"+str(+self.año)
        
#print(Fecha(15,12,2001).Comparar_Fechas(Fecha(15,12,2002)))