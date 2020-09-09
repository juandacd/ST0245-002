class Nodo():
    
    def __init__(self, Obj=None, nxt= None):
        self.Obj = Obj
        self.nxt = nxt
        
        
class Lista_Simple_enlazada():
    
    def __init__(self, size = 0):
        self.first_Nodo = None
        self.size = size
        
    def __void(self):
        return self.fisrt_Nodo == None
       
    def size(self):
        return self.size
   
    def contains(self, element):
        UnNodo = self.first_Nodo
        while(UnNodo != None):
            if(UnNodo.obj == element):                 
                return True
            UnNodo = UnNodo.nxt
        return False
    
    def insert(self, element, index):
        self.size=self.size+1
        n = Nodo(element)
        if(index>self.size):
            UnNodo=self.first_Nodo
            n.nxt=UnNodo
            self.first_Nodo = n
            return
        if not(self.first_Nodo):
            self.first_Nodo = Nodo(obj=element)
            return
        prev = None
        UnNodo = self.first_Nodo
        x=0 
        while(UnNodo.nxt and x<index):
            prev = UnNodo
            UnNodo = UnNodo.nxt
            x=x+1
        n.nxt=UnNodo
        if(prev is None):
            self.first_Nodo = n
        else:
            prev.nxt=n
    
    def remove(self, element):
        UnNodo = self.first_Nodo
        prev = None
        while(UnNodo and UnNodo.obj != element):
            prev = UnNodo
            UnNodo = UnNodo.nxt
        if(prev is None):
            self.head = UnNodo.nxt
        elif UnNodo:
            prev.nxt = UnNodo.nxt
            UnNodo.nxt = None