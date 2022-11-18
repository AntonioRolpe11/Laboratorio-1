'''
Created on 9 nov 2022

@author: anton
'''

from __future__ import annotations
from typing import TypeVar, Generic
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from us.lsi.tools.Preconditions import check_argument


E = TypeVar('E')

class Matriz(Generic[E]) :
    
    def __init__(self, datos:list[list[E]]) -> None:
        self.__datos = datos
        for i in range(len(self.datos)):
                check_argument(len(self.datos[0]) == len(self.datos[i]),f'El numero de columnas debe ser el mismo en todas las filas')
                check_argument(len(self.datos)>=0 and len(self.datos[i])>=0, f'El numero de filas y columnas debe de ser mayor que 0')
                
    @property
    def datos(self)->list[list[E]]:
        return self.__datos
    
    @staticmethod
    def of(datos:list[list[E]]) -> Matriz[E]:   
        return Matriz(datos)
    
    @staticmethod
    def of_file(file:str, t:callable[[str],E]=lambda x:int(x)) -> Matriz[E]:
        
        ls = lineas_de_fichero(file)
        
        ls = [i.split(' ') for i in ls]
    
        lf = []
    #afoiafsoif
        for i in range(len(ls)):
        
            lf += [[t(j) for j in ls[i]]]
        
        return Matriz(lf)
       
    @property    
    def nf(self) -> int:
        return int(len(self.datos))
    
    @property
    def nc(self) -> int:
        return int(len(self.datos[0]))
    
    def get(self,f:int,c:int)->E: 
        fila = self.datos[f-1]
        return fila[c-1]
    
    @property
    def traspuesta(self)-> Matriz:
        lf = []
        
        lon = len(self.datos)
        
        for m in range(lon):
            
            lf += [[i[m] for i in self.datos]]
                    
        return Matriz(lf)
    
    @property
    def es_simetrica(self) -> bool:
        if self.datos == self.traspuesta.datos:
            a = True
        else:
            a = False
        return a
        
    def submatriz(self,f1:int,c1:int,f2:int,c2:int) -> Matriz[E]:    
        check_argument(0<=f1<f2<len(self.datos), f'f1 tiene que ser menor que f2 y el numero de filas y mayor que cero')
        check_argument(0<=c1<c2<len(self.datos[0]), f'c1 tiene que ser menor q c2 y que el numero de columnas y mayor que cero') 
        
        lf = []
        
        for i in range(f1-1,f2):
            lf += [[self.datos[i][j]for j in range(c1-1,c2)]]
            
        return Matriz(lf)
    
    def __str__(self) -> str:
        
        m = len(self.datos)
        
        cad = ''
        
        for i in range(m):
        
            cad += ('\t'.join(f'{x}' for x in self.datos[i]) + '\n')

        return cad
                
                  
   
    def __eq__(self,other:Matriz) -> bool:
        
        check_argument(isinstance(other, Matriz), f'Los dos parametros deben de ser tipo Fraction_Matriz.')
        
        if self.datos == other.datos:
            a = True
        else:
            a = False
        return a
        
        
if __name__ == '__main__':
    
    a = Matriz.of([[1,4],[9,7]])
    
    b = Matriz.of([[0,1,4],[1,2,1],[4,1,8]])
    
    
    c = Matriz.of_file('C:/Users/anton/git/Laboratorio-1/src/lab/ficheros/matriz_enteros.txt')
    
    print(b)
    
    print(c)
    
    print(a.traspuesta)
    
    print(b.submatriz(1, 1, 3, 3))
    
    

    
    
    
    
    
    