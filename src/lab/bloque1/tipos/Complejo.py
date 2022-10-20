'''
Created on 18 oct 2022

@author: anton
'''

from __future__ import annotations
from dataclasses import dataclass
from math import atan2

@dataclass (frozen = True , order = True)
class Complejo:
    
    re: float
    im:float
    
    
    @staticmethod
    def of(re:float,im:float) -> Complejo:
        return Complejo(re,im)
    
    @staticmethod
    def of_re(re:float) -> Complejo:
        return Complejo(re,0)
    
    @staticmethod
    def parse(cadena:str) -> Complejo:
        st = ''
        lista = []
        for i in cadena:
            if i == '+' or i == '-' or i == 'i':
                list.append(float(st))
            st = st + i
        if len(list) == 1:
            return Complejo(float(list[0]))
        else:
            return Complejo(float(list[0], float(list[1])))
                
        

        
        
        return Complejo(float(lista[0]),float(lista[:-1])) 
    
    
    
        
        
        
        
        
        
        
        
        
            

    
    @property
    def abs(self) -> float:
        return (self.re**2+self.im**2)**(1/2)
    
    def arg(self) -> float:
        return atan2(self.re,self.im)
    
    def conjugado(self) -> Complejo:
        pass                                 

if __name__ == '__main__':
    pass