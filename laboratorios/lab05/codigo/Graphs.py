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