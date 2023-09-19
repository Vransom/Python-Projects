class Protected:
    def __init__(self): 
        self._protectedVar=0 
        self.__privateVar=20
        
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar=private

obj=Protected() #sets protected object
obj._protectedVar=1234
print(obj._protectedVar)

obj.getPrivate()
obj.setPrivate(5678) #sets private object
obj.getPrivate()
