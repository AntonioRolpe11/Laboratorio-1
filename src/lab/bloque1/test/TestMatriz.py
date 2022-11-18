'''
Created on 9 nov 2022

@author: anton
'''

from src.lab.bloque1.tipos.Matriz import *


if __name__ == '__main__':
    
    m1 = Matriz.of_file('C:/Users/anton/git/Laboratorio-1/src/lab/ficheros/matriz_caracteres.txt',t=lambda x: str(x))
    
    m2 = Matriz.of_file('C:/Users/anton/git/Laboratorio-1/src/lab/ficheros/matriz_enteros.txt',)
    
    print('La matriz leída desde el fichero matriz_caracteres.txt es:')
    print('-'*40)
    print(m1)
    print('-'*40)
    print()
    
    
    print('La traspuesta de la matriz anterior es:')
    print('-'*40)
    print(m1.traspuesta)
    print('-'*40)
    print()
    
    print('¿Es una matriz simétrica? -->',m1.es_simetrica)
    print('La matriz leída desde el fichero matriz_enteros.txt es:')
    print('-'*40)
    print(m2)
    print('-'*40)
    print()
    
    print('El número de filas de la matriz es', m2.nf, 'y el número de columnas', m2.nc,end='.\n')
    print('¿Es una matriz simétrica? -->',m2.es_simetrica)
    
    
    
    