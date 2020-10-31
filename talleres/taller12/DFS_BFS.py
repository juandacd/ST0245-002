class GraphAl:
    
    def __init__(self,size):
        self.size = size
        self.lista = [[] for i in range(size)]

    def __repr__(self):
        return '{}'.format(self.lista)

    def addArc(self, source, destination):
        self.lista[source].append(destination)
        self.lista[destination].append(source)
        

    def getSuccessors(self, vertice):
        succs = []
        for c in self.lista[vertice]:
            succs.append(c)
        return succs

    def DFS(self, i, j):
      visited = [False] * self.size 
      self.DFSaux(i,j, visited)
    
    def DFSaux(self, i, j, visited):
      visited[i] = True
      for a in self.lista[i]:
          if(not visited[a]):
              if(a == j):
                  print("Sí hay camino")
                  self.DFSaux(a, j, visited)

    def BFS(self, i, j):
      visited = [False]* self.size
      q = []
      q.append(i)
      visited[i] = True
      while(len(q) != 0):
          for a in self.lista[i]:
              if(not visited[a]):
                  if(a == j):
                      print("Sí hay camino")
                  q.append(a)
                  visited[a] = True


ga = GraphAl(5)
ga.addArc(0, 3)
print(ga)
ga.addArc(1,4)
ga.addArc(3,4)
ga.addArc(0,4)
print(ga)
print(ga.getSuccessors(1))
ga.DFS(0,4)