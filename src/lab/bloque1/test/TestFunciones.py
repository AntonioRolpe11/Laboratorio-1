'''
Created on 17 oct 2022

@author: anton

'''

from lab.bloque1.funciones.Funciones import producto, combinatorio, calcular_s, newton

if __name__ == '__main__':
    
    print(producto(5,5))
    
    print(combinatorio(4, 2))
    
    print(calcular_s(4,2))
    
    print(newton('2x**2','4x',3,0.001))