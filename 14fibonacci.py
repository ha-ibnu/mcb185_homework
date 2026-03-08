def fib(lim):
	a = 0
	b = 1
	print(a)
	print(b)
	for i in range(lim-2):
		c = a + b
		print(c)
		a = b
		b = c
	return
fib(10)

