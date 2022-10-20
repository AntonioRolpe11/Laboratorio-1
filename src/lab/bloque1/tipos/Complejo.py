'''
Created on 18 oct 2022

@author: anton
'''

from __future__ import annotations
from dataclasses import dataclass
from math import atan2
from pickle import FALSE, TRUE

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
        
        suma = False
        resta = False
        for i in cadena:
            if i=='+':
                suma = True 
            else:
                resta = True 
        if suma == True:
            lista = cadena.split('+')
        else :
            lista = cadena.split('-')            
                    
        n = lista[0]
        l = lista[-1].replace('i','')
        return Complejo(float(n),float(l)) 
            

    @property
    def abs(self) -> float:
        return (self.re**2+self.im**2)**(1/2)
    
    def arg(self) -> float:
        return atan2(self.re,self.im)
    
    def conjugado(self) -> Complejo:
        pass                                 

if __name__ == '__main__':
    pass