'''
Created on 19 oct 2022

@author: anton
'''
from lab.bloque1.tipos.Complejo import Complejo 





if __name__ == '__main__':
    
    ng = Complejo.of(1,-9)
    
    r = '5.8 - 233.35i'
    
    n = Complejo.parse(r)
    
    print(n)
    
    print(ng)
    