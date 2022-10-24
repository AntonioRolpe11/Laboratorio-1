
'''
Created on 17 oct 2022

@author: anton
'''

from us.lsi.tools.Preconditions import check_argument
from typing import Callable

def producto(n:int,k:int) -> int:
    check_argument(n > 0 and k > 0, f'n y k deben de ser positivos')
    check_argument(n < k , f'n debe de ser mayor que k')
    
    x = 1
    for i in range(0,k):
        x = x*(n-i) 
    return x


def combinatorio(n:int,k:int) -> float:
    
    check_argument(n > 0 and k > 0, f'n y k deben de ser positivos')
    check_argument(n < k , f'n debe de ser mayor que k')
    
    primero = producto(n,n)
    segundo = producto(k,k)
    otro = n-k
    denm = producto(otro, otro)
    
    return primero/(segundo*denm)

def calcular_s(n:int,k:int) -> float:
    check_argument(n > 0 and k > 0, f'n y k deben de ser positivos')
    check_argument(n < k , f'n debe de ser mayor que k')
    
    fact_k = producto(k,k)
    sumatorio = 0
    for i in range(0,k+1):
        sumatorio = sumatorio + (((-1)**i)*combinatorio(k,i)*(k-i)**n)
    return (1/fact_k)*sumatorio

def newton(funcion:Callable,der:Callable,a:float,error:float):
    
    fun:float = lambda x : funcion
    der_fun:float = lambda x : der
    
    x0 = a

    error_actual = False
    
    while error_actual == False:
        
        raiz = float(x0-float(fun(x0)))/float(der_fun(x0))
        
        error_bucle= abs(raiz-x0)/raiz
        
        if error_bucle<error:
            error_actual = True
                    
        x0 = raiz
        
    return x0
        
        
    
    
    
    

if __name__ == '__main__':
    pass