#Practice iteration
def triangular(n):
    if not isinstance(n, (int, float)) or n <= 0: return None
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(triangular(100))
print(triangular(50))
print(triangular(0))
print(triangular(5))

def fac(n):
    if n <= 0 : return 1
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac

print(fac(5))  
print(fac(0))  
print(fac(-4)) 

import math 

def nchoosek(n, k): 
    return fac(n) / (fac(k) * fac(n -k))

def poisson(n, k):
    return n**k * math.e**-n / fac(k)

def euler(lim):
    e = 0
    for n in range(lim):
        e = e + 1 / fac(n)
    return e

def is_prime(n):
    for den in range(2, n//2):
        if n % den == 0: return False
    return True

def nilakantha(lim):
    pi = 3
    for i in range(1, lim+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d # if even , sym - 
        else:          pi = pi + 4 / d # and odd , sym +
    return pi