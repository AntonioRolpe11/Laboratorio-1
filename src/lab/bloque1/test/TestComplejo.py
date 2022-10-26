'''
Created on 19 oct 2022

@author: anton
'''
from lab.bloque1.tipos.Complejo import Complejo 





if __name__ == '__main__':
    
    c1 = Complejo.of(5.7,5)
    
    c2_0 = '-5 -7i'
    
    c2 = Complejo.parse(c2_0)
    
    print('#'*40)
    print('TEST DE LA FACTORIA:')
    print('El primer número complejo definido es: c1 =',c1,'\n')
    
    print('#'*40)
    print('TEST DE LA FUNCION PARSE:')
    print('El primer número complejo definido es: c2 =',c2,'\n')
    
    print('#'*40)
    print('TEST DE EQUALS:')
    print('¿Son iguales c1 y c2? -->', c1==c2,'\n')
    
    print('#'*40)
    print('TEST DE ALGUNAS PROPIEDADES:')
    print('El argumento de c1 es:', c1.arg)
    print('El módulo de c2 es:', c2.abs,'\n')
    
    print('#'*40)
    print('TEST DE ALGUNAS FUNCIONES:')
    print('La suma entre c1 y c2 es:', c1+c2)
    print('El producto entre c1 y c2 es:', c1*c2)
    print('La division entre c1 y c2 es:', c1/c2,'\n')
    
     
    
    
    

    
    