'''
Created on 18 oct 2022

@author: anton
'''

def producto(n:int,k:int) -> int:
    x = 1
    for i in range(0,k):
        x = x*(n-i)
    return x

def combinatorio(n:int,k:int) -> float:
    fact_n = 1
    fact_k = 1
    fact_n_k = 1  
    for i in range(1,n+1):
        fact_n = fact_n * i
    for i in range(0,k+1):
        fact_k = fact_k * i
    for i in range(0,(n-k)+1):
        fact_n_k =  fact_n_k * i
        
    return fact_n/(fact_k*fact_n_k)

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