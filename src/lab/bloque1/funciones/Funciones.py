
'''
Created on 17 oct 2022

@author: anton
'''

def producto(n:int,k:int) -> int:
    x = 1
    for i in range(0,k):
        x = x*(n-i) 
    return x


def combinatorio(n:int,k:int) -> float:
    primero = producto(n,n)
    segundo = producto(k,k)
    otro = n-k
    denm = producto(otro, otro)
    
    return primero/(segundo*denm)

def calcular_s(n:int,k:int) -> float:
    fact_k = producto(k,k)
    sumatorio = 0
    for i in range(0,k+1):
        sumatorio = sumatorio + (((-1)**i)*combinatorio(k,i)*(k-i)**n)
    return (1/fact_k)*sumatorio

def newton():
    pass

if __name__ == '__main__':
    pass