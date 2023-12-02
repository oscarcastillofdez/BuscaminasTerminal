class casilla:
    def __init__(self):
        self.estado = False
        self.mina = False
        self.val = 0

    def convertirMina(self):
        self.mina = True

    def aumentarVal(self):
        self.val = self.val + 1

    def getVal(self) -> int:
        if (self.mina == True):
            return 0
        else:
            return self.val
    
    def mostrar(self):
        if (self.estado == True):
            return -2
        self.estado = True
        if (self.mina == True):
            return -1
        else:
            return self.val
        
    def print(self):
        if (self.estado == False):
             print("[X]",end= " ")
        else: 
            if (self.mina == True):
                print("[O]",end= " ")
            else: 
                if (self.val == 0):
                    print("[ ]",end= " ")
                else:
                    print("["+ str(self.val) +"]",end= " ")
    
    

        
    

