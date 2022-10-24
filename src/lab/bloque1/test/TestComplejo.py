'''
Created on 19 oct 2022

@author: anton
'''
from lab.bloque1.tipos.Complejo import Complejo 





if __name__ == '__main__':
    
    c1 = Complejo.of(5.7,5)
    
    c2 = Complejo.of(5,7) 
    
    r = '5.8 - 233.35i'
    
    n = Complejo.parse(r)
    
    print(Complejo.parse('57 + 98.9i'))
    
    print(c1.conjugado())
    
    print(c1+c2)
    
    print(c1*c2)
    
    print(c1/c2)
    
    print(c1==c2)
    

    
    