# 10demo.py by Ibnu

import math

print("hello, again") #greeting
print(1.5e-64)

print(pow(2,3))

print(round(2.4355553, ndigits=3))

print(round((2**0.5), ndigits=2))

print(pow(2, 3))

print("print(math.bla bla)")
print(math.inf)

print(math.pow(2, 7))

print(math.sqrt(8))

print(round(math.log(3.6), ndigits = 2))

print()
## NUMBERS

print("#numbers")
print(0.1*1)
print(0.1*5)
print("kida was my husband")

print("="*50)
## Variable 
print('#Variable')
a =3                        #side of triangle
b =4                        #side of triangle
c =math.sqrt(a**2 + b**2)   #hypotenuse
print(c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep =' ', end=' $$\n')
print(sep=' ', end='\n')
print("="*50)
## Functions 
print('#Function')

def pytho(a,b):
    c = math.sqrt(a**2+b**2)
    return c

hyp = pytho(4, 7)
hyp1 = pytho(3, 4)
print(hyp, hyp1, sep=(";"))

#simplified
def pytho(a,b):
    return math.sqrt(a**2+b**2)
print(pytho(5, 8))
