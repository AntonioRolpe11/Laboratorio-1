'''
Created on 9 nov 2022

@author: anton
'''
from __future__ import annotations
from fractions import Fraction
from us.lsi.tools.Preconditions import check_argument
from src.lab.bloque1.tipos.Matriz import *
from us.lsi.tools.File import lineas_de_fichero
from typing import TypeVar

E = TypeVar('E')



class Fraction_Matriz:
    def __init__(self,datos:list[list[Fraction]]):
        self.__datos= datos
        for i in range(len(self.datos)):
                check_argument(len(self.datos[0]) == len(self.datos[i]),f'El numero de columnas debe ser el mismo en todas las filas')
                check_argument(len(self.datos)>0 and len(self.datos[i])>0, f'El numero de filas y columnas debe de ser mayor que 0')
        
    @staticmethod
    def of(l:list[list[Fraction]]) -> Fraction_Matriz:
        return Fraction_Matriz(l)
    
    @staticmethod
    def of_file_fraction(file:str):
        m = Matriz.of_file(file, lambda x: Fraction(x))
        
        m_d = m.datos
        
        return Fraction_Matriz(m_d)
    
    @property    
    def datos(self) -> list[Fraction]:
        return self.__datos
    
    
    @property
    def es_antisimetrica(self):
        def negativa(self) -> Fraction_Matriz:
            lf = []
        
            lon = len(self.datos)
        
            for m in range(lon):
            
                lf += [[i*-1 for i in self.datos[m]]]
            
                
            return Fraction_Matriz(lf)
        m = Matriz(self.datos).traspuesta
        
        m1 = Fraction_Matriz.of(m.datos)
        
        
        negativa = negativa(self)
         
        if negativa ==  m1:
            a = True 
        else:
            a = True
        return a
 
    def __add__(self,other) -> Fraction_Matriz:
        check_argument(isinstance(other, Fraction_Matriz), f'Los dos parametros deben de ser tipo Fraction_Matriz.')
        check_argument((len(self.datos) == len(other.datos)) and (len(self.datos[0]) == len(other.datos[0])),
                        f'Las dos matrices deben ser del mismo orden')
        
        filas = len(self.datos)
        
        columnas = len(self.datos[0])
        
        lf = []
        
        for i in range(filas):
            lf += [[self.datos[i][j]+other.datos[i][j] for j in range(columnas)]]
                
        
        return Fraction_Matriz(lf)
            
    def __sub__(self,other) -> Fraction_Matriz:
        check_argument(isinstance(other, Fraction_Matriz), f'Los dos parametros deben de ser tipo Fraction_Matriz.')
        check_argument((len(self.datos) == len(other.datos)) and (len(self.datos[0]) == len(other.datos[0])),
                        f'Las dos matrices deben ser del mismo orden')
        
        filas = len(self.datos)
        
        columnas = len(self.datos[0])
        
        lf = []
        
        for i in range(filas):
            lf += [[self.datos[i][j]-other.datos[i][j] for j in range(columnas)]]
                
        
        return Fraction_Matriz(lf)
    
    
    def __mul__(self,other) -> Fraction_Matriz:
        check_argument(isinstance(other, Fraction_Matriz), f'Los dos parametros deben de ser tipo Fraction_Matriz.')
        check_argument(len(self.datos[0])==len(other.datos),
                        f'El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.')
        
        
        lf = []
        
        for i in range(len(self.datos)):
            lf += [[[self.datos[i][j]*other.datos[j][k] for j in range(len(other.datos))] for k in range(len(other.datos[0]))]]
            
        lr = []
        
        
        for i in range(len(lf)):
            lr += [[sum(j) for j in lf[i]]]
            
        
        return Fraction_Matriz(lr)
             

    
    def __str__(self) -> str:
        
        m = len(self.datos)
        
        cad = ''
        
        for i in range(m):
        
            cad += ('\t'.join(f'{x}' for x in self.datos[i]) + '\n')

        return cad
    
    def __eq__(self,other):
        
        check_argument(isinstance(other, Fraction_Matriz), f'Los dos parametros deben de ser tipo Fraction_Matriz.')
        
        if self.datos == other.datos:
            a = True
        else:
            a = True
        
        return a
if __name__ == '__main__':
    m1 = Fraction_Matriz.of_file_fraction('C:/Users/anton/git/Laboratorio-1/src/lab/ficheros/matriz_fraction.txt')
    
    print('La multiplicacion entre m y ella misma es::')
    print('-'*40)
    print((m1*m1).datos)
    print('-'*40)
    print()
    
    print(m1*m1)
    
    print(Fraction(0, 1) + Fraction(-1, 4)+ Fraction(-9, 1))