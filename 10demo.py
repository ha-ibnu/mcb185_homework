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

def pytho(a,b): return math.sqrt(a**2+b**2)

""" Tips and tricks,
knowing your purposes and start write code,
do not much thinking just write, keep your hand and brain work
at the same times, after that simplify it."""

print("="*50)
print()
print("#Function Practice")
print()
print("#Example")
print("1. Area of circle")
def crc_a(r): return math.pi * r**2
print(crc_a(38))
print()
print("2. Area of rectangle")
def rec_a(a,b): return a * b
print(rec_a(7,4.1))
print()
print("3. Area of triangle")
def tri_a(a,b): return rec_a(a,b)/2
print(tri_a(2,3))
print()
print("#Practice")
print()
print("1. Conversion F to C, vice-versa")
def temp_f(c): return (c*9/5)+32
def temp_c(f): return (f-32)*5/9
def temp(val, unit):
    if unit == "C":
        return val * 9/5 + 32
    elif unit == "F":
        return (val - 32) * 5/9
    else:
        return "error"


print(temp_f(4), temp_c(100), sep="; ")
print(temp(4, "C"), temp(100, "F"), sep="; ")
print()
print("2. Conversion speed MPH to KPH, vice-versa")
def speed(val, unit):
    if unit == "MPH":
        return val * 1.60934
    elif unit == "KPH":
        return val / 1.60934
    else:
        return "error"
print(round(speed(4, "KPH")), round(speed(100, "MPH")), sep="; ")

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance(2,3,-1,2))