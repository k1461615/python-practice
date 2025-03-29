# https://projecteuler.net/problem=2

fib1 = 1
fib2 = 2
sum = 0
while fib2 < 4000000:
	if fib2 % 2 == 0:
		sum += fib2	
	curFib = fib1 + fib2
	fib1 = fib2
	fib2 = curFib
print(sum)

