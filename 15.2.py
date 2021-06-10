from math import log1p, cos

def f12(x):
	if (x < 114):
		return log1p(pow(x, 3) - pow(x, 5) - 51) + pow(x, 3) - 44
	elif (114 <= x < 125):
		return 93*pow(x, 7) + 66*pow(x, 2) + 57
	elif (x >= 125):
		return 31 * pow((cos(x) + pow(x, 4)/79), 8) + cos(x)

print(f'{f12(118):.2e}')
print(f'{f12(139):.2e}')