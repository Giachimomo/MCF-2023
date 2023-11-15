import numpy as np
class hit:
    def __init__(self,a,b,c):
        self.modulo=a
        self.sensore=b
        self.tempo=c 
    def __lt__ (self,other):
        if self.tempo<other.tempo:
            return True
        elif self.tempo==other.tempo:
            if self.modulo<other.modulo:
                return True
            elif self.modulo==other.modulo:
                if self.sensore<other.sensore:
                    return True
        return False
    def __add__(self,other):
        return self.tempo+other.tempo
    def __sub__(self,other):
        return self.tempo-other.tempo
    def __str__(self):
        return '{:}'.format(self.tempo)
    
