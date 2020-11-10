import numpy as np

class Graph():
    
    def __init__(self, vertices):
        self.size = vertices
        
    def addArc(sefl, source, destination, weight):
        pass
    
    def getSuccesors(self, vertice):
        pass
    
    def getWeight(self, source, destination):
        pass
    
    def getSize(self):
        return self.size


class GraphAM(Graph):
    
    def __init__(self, vertices):
        Graph.__init__(self, vertices)
        self.Mat = np.array(self.size*[self.size*[0]])
    
    def addArc(self, source, destination, weight):
        self.Mat[source][destination] = weight 
    
    def getSuccessors(self, vertice):
        siguiente = []
        for i in range(self.size):
            if(self.Mat[vertice][i] != 0):
                siguiente.append(i)
        return siguiente
    
    def getWeight(self, source, destination):
        return self.Mat[source][destination]
    
    
class GraphAl:
    
    def __init__(self,size):
        self.size = size
        self.lista = [[] for i in range(size)]

    def addArc(self, source, destination):
        self.lista[source].append(destination)
        self.lista[destination].append(source)
        
    def isBicolorable(self, i):
      visited = [""]* self.size
      q = []
      q.append(i)
      visited[i] = "Blue"
      while( len(q) != 0):
        b = q.pop()
        for a in self.lista[b]:
          if(visited[a] == "" and visited[b] == "Blue"):
            q.append(a)
            visited[a] = "Red"
          if(visited[a] == "Red" and visited[b] == "Red"):
            print("IS NOT BICOLORABLE")
            return        
      print("IS COLORABLE") 

    
gf = GraphAl(9)
gf.addArc(0,1)
gf.addArc(0,2)
gf.addArc(0,3)
gf.addArc(0,4)
gf.addArc(0,5)
gf.addArc(0,6)
gf.addArc(0,7)
gf.addArc(0,8)
gf.isBicolorable(0)
