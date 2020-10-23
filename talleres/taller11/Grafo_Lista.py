class Grafo_Listas:
    
    def __init__(self, size):
        self.size = size
        self.lista = [[] for i in range(size)]

    def __repr__(self):
        return '{}'.format(self.lista)

    def getWeight(self, source, destination):
        for d in self.lista[source]:
            if d[source] == destination:
                return d[source]

    def addArc(self, source, destination, weight):
        self.lista[source].append((destination, weight))

    def getSuccessors(self, vertice):
        succs = []
        for d in self.lista[vertice]:
            succs.append(d)
        return succs

    
ga = Grafo_Listas(3)
ga.addArc(0, 3, 10)
print(ga)
print(ga.getWeight(0, 3))
ga.addArc(0, 4, 7)
print(ga)
print(ga.getSuccessors(0))