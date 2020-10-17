class Nodo:
    
    def __init__(self, Dato):
        self.Izquierda = None
        self.Derecha = None
        self.Dato = Dato

    def __repr__(self):
        return f'{self.Dato}'


class ArbolBinario:
    
  def __init__(self):
      self.Raiz = None
    
  def insertar(self, Dato):
    if self.Raiz is None:         
      self.Raiz = Nodo(Dato)       
    else:
      self.__insertar_aux(Dato, self.Raiz)  #O(log2 n)+
                                           
  def __insertar_aux(self, Dato, actual):
      if(actual.Derecha is None or actual.Izquierda is None):
        if(Dato > actual.Dato):
          actual.Derecha = Nodo(Dato)
        else:
          actual.Izquierda = Nodo(Dato)
      else:
        if(Dato > actual.Dato):
            self.__insertar_aux(Dato, actual.Derecha)
        else:
            self.__insertar_aux(Dato, actual.Izquierda)
      return actual
       
  def buscar(self, Dato):
      return self.__buscar_aux(Dato, self.Raiz) #O(log2 n)

  def __buscar_aux(self, Dato, actual):
      if(actual is None):
          return False
      else:
          if(Dato == actual.Dato):
              return True
          else:
              if(Dato > actual.Dato):
                  return self.__buscar_aux(Dato, actual.Derecha)
              else:
                  return self.__buscar_aux(Dato, actual.Izquierda)
     
  def imprimir(self):
      self.__imprimir_aux(self.Raiz)
        
  def __imprimir_aux(self, actual):
      if actual is not None:
          self.__imprimir_aux(actual.Izquierda)
          print(actual.Dato)
          self.__imprimir_aux(actual.Derecha)
  
Arbol = ArbolBinario()
Arbol.insertar(4)
Arbol.insertar(3)
Arbol.insertar(5)
print(Arbol.buscar(3))
Arbol.imprimir()