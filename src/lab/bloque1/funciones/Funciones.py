
'''
Created on 17 oct 2022

@author: anton
'''

def producto(n:int,k:int) -> int:
    x = 1
    for i in range(0,k):
        x = x*(n-i)
    return x

def fact(n:int)->int:
    res = 1
    for i in range(1,n+1):
        res = res*i
    return res

def combinatorio(n:int,k:int) -> float:
    n = fact(n)
    k = fact(k)
    n_k =  fact(n-k)
    
    return n/(k*n_k)

def calcular_s(n:int,k:int) -> float:
    fact_k = 1
    sumatorio = 0
    for i in range(0,k+1):
        fact_k = fact_k * i
    for i in range(0,k+1):
        sumatorio = sumatorio + (((-1)**i)*combinatorio(k,i)*(k-1)**n)
    return (1/fact_k)*sumatorio

def newton():
    pass

if __name__ == '__main__':
    pass