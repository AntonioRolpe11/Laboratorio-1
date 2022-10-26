
'''
Created on 17 oct 2022

@author: anton
'''

from us.lsi.tools.Preconditions import check_argument
from typing import Callable 


def producto(n:int,k:int) -> int:
    check_argument(n >= 0 and k >= 0, f'n y k deben de ser positivos')
    check_argument(n >= k , f'n debe de ser mayor o igual que k')
    
    x = 1
    for i in range(0,k):
        x = x*(n-i) 
    return x


def combinatorio(n:int,k:int) -> float:
     
    check_argument(n >= 0 and k >= 0, f'n y k deben de ser positivos')
    check_argument(n > k or n==k , f'n debe de ser mayoro igual que k')
    
    primero = producto(n,n)
    segundo = producto(k,k)
    otro = n-k
    denm = producto(otro, otro)
    
    return primero/(segundo*denm)

def calcular_s(n:int,k:int) -> float:
    check_argument(n > 0 and k > 0, f'n y k deben de ser positivos')
    check_argument(n >= k , f'n debe de ser mayor o igual que k')
    
    fact_k = producto(k,k)
    sumatorio = 0
    for i in range(0,k+1):
        sumatorio = sumatorio + (((-1)**i)*combinatorio(k,i)*(k-i)**n)
    return (1/fact_k)*sumatorio

def newton(f:Callable,der_f:Callable,a:float,error:float):
    pass
         


if __name__ == '__main__':
    pass