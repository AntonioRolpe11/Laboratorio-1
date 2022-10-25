'''
Created on 18 oct 2022

@author: anton
'''

from __future__ import annotations
from dataclasses import dataclass
from math import atan2
from us.lsi.tools.Preconditions import check_argument



@dataclass (frozen = True , order = False)
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
            lista = cadena.split(' ',1)            
                    
        n = lista[0]
        l = lista[-1].replace('i','')
        l2 = l.replace(' ','')
        return Complejo(float(n),float(l2)) 
    
    def __add__(self,other:Complejo) -> Complejo:
        return Complejo(self.re+other.re,self.im+other.im)
    
    def __sub__(self,other:Complejo) -> Complejo:
        return Complejo(self.re-other.re,self.im-other.im)      
    
    def __mul__(self,other:Complejo) -> Complejo:
        return Complejo(self.re*other.re-self.im*other.im,self.re*other.im+self.im*other.re)  
    
    def __truediv__(self,other:Complejo) -> Complejo:
        return Complejo((self.re*other.re+self.im*other.im)/(other.re**2+other.im**2)    \
                        ,(self.im*other.re-self.re*other.im)/(other.re**2+other.im**2))
        
    def __eq__(self,other:Complejo) -> bool:
        return (self.re==other.re) and (self.im==other.im)
    
    def __str__(self) -> str:
        if self.im < 0 and self.re!=0:
            return f'{self.re} - {abs(self.im)}i'
        elif self.im>0 and self.re!=0:
            return f'{self.re} + {self.im}i'
        elif self.re==0:
            return f'{self.im}i'
        else:
            return f'{self.re}'
            

    @property
    def abs(self) -> float:
        return (self.re**2+self.im**2)**(1/2)
    
    @property
    def arg(self) -> float:
        return atan2(self.re,self.im)
    
    @property 
    def conjugado(self) -> Complejo:
        if self.im==0:
            return Complejo(self.re)
        else:
            return Complejo(self.re,-self.im)
    
    
        

if __name__ == '__main__':
    pass