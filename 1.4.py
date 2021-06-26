from math import sin

def f14(n):
	if n == 0:
		return 4
	elif n == 1:
		return 2
	else:
		return abs(f14(n - 1)) + sin(f14(n - 1)) - 20

print(f'{f14(6):.2e}')
print(f'{f14(14):.2e}')
