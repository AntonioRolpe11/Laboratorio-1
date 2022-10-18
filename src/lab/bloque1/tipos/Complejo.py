'''
Created on 18 oct 2022

@author: anton
'''

from __future__ import annotations
from dataclasses import dataclass
from math import atan2

@dataclass
class Complejo (frozen=True, order=False):
    
    re: float
    im: float
    
    @staticmethod
    def of(re:float,im:float) -> Complejo:
        return Complejo(re,im)
    
    @staticmethod
    def of_re(re:float) -> Complejo:
        return Complejo(re,0)
    
    @staticmethod
    def parse(text:str) -> Complejo:
        lista = text.split('+','-')
        
        return Complejo(lista[0],lista[:-1]) 
            

    
    @property
    def abs(self) -> float:
        return (self.re**2+self.im**2)**(1/2)
    
    def arg(self) -> float:
        return atan2(self.re,self.im)
    
    def conjugado(self) -> Complejo:
        pass                                 

if __name__ == '__main__':
    pass