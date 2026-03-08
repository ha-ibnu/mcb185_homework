import math

n=100

def triangular(n):
	tri = 0
	for i in range(n+1):
		tri = tri +1
	return tri

print(f'n={n} triangular={triangular(n)}')

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n+1):
		fac = fac * i
	return fac

print(f'n={n} fac={factorial(n)}')

k = 100
def poisson(n, k):
	return n**k * math.e**-n / factorial(k)

print(f'n={n} and k={k} poisson={poisson(n, k)}')

def nchoosek(n, k):
	return factorial(n) /(factorial(k) * factorial(n - k))

print(f'n={n} and k={k} nchoosek={nchoosek(n, k)}')

def euler(lim):
	e = 0
	for n in range(lim):
		e = e +1/factorial(n)
	return e

print(f'lim={n} euler={euler(n)}')

def is_prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False
		return True

print(f'n={n} is prime? {is_prime(n)}')

def nilakantha(lim):
	pi = 3
	for i in range(1, lim+1):
		n = 2 * i
		d = n * (n+1) * (n+2)
		if i % 2 == 0: pi = pi - 4 / d
		else:		   pi = pi + 4 / d
	return pi

print(f'nilakhanta={n} pi={nilakantha(n)}')














