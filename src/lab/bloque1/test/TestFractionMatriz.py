'''
Created on 9 nov 2022

@author: anton
'''

from src.lab.bloque1.tipos.Fraction_Matriz import *

        
if __name__ == '__main__':
    m1 = Fraction_Matriz.of_file_fraction('C:/Users/anton/git/Laboratorio-1/src/lab/ficheros/matriz_fraction.txt')
    
    
    
    print('La matriz leída desde el fichero matriz_caracteres.txt es:')
    print('-'*40)
    print(m1)
    print('-'*40)
    print()
    
    print('¿Es antisimétrica? -->',m1.es_antisimetrica)
    print('La suma entre m y ella misma es:')
    print('-'*40)
    print(m1+m1)
    print('-'*40)
    print()
    
    print('La multiplicacion entre m y ella misma es::')
    print('-'*40)
    print(m1*m1)
    print('-'*40)
    print()
    
    print('La diferencia entre m y ella misma es:')
    print('-'*40)
    print(m1-m1)
    print('-'*40)
    print()
    
    