import numpy as np
 
class ArrayList:

    __DEFAULT = 10
    
    def __init__(self):
        self.__DEFAULT = 10
        self.__size = 0
        self.__elements = np.array([0]*self.__DEFAULT)
 
    def size(self):
        return self.__size
 
    def get(self, index):
        if(index >= 0 and index < self.__size):
            return self.__elements[index]
 
    def add(self, o):
        self.__elements[self.__size] = o
        self.__size+=1
 
    def addInIndex(self, index, o):
        if(index >= o and index < self.__size):
            for i in range (self.__size):
                if(i == len(self.__lements) and i == self.__size):
                    self.extend()              
                if(index == i):
                    K = self.__elements[i]
                    self.__elements[i] = o
                    self.__elements[i+1] = K
                    self.__size += 1               
        else:
            if(index == self.__size):
                self.__elements[index] = o
                self.__size +=1
            if(self.__size == len(self.__elements)):
                self.extend()
                
    def extend(self):
        elementsnew = np.array([0]*(len(self.__elements) + self.__DEFAULT))
        for j in range (self.__size):
           elementsnew[j] = self.__elements[j]
           self.__elements = elementsnew
                
                
MiArray = ArrayList()
MiArray.add(-1)
MiArray.add(99)
print(MiArray.size())
print(MiArray.get(0))
