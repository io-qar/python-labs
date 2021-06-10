from math import log1p

def f13(n, m):
	a = 0
	b = 0

	for i in range(1, n + 1):
		for j in range (1, m + 1):
			a += log1p(i) + pow(i, 4) - 73

	for i in range(1, n + 1):
		b += 27*pow(i, 2) + 39*pow(i, 8) - 10

	return (a/43) + 28*b

print(f'{f13(85, 99):.2e}')
print(f'{f13(79, 24):.2e}')
