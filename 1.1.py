from math import cos, log1p, tan

def f11(x, y, z):
	return (math.cos(61*z - 26*pow(y, 3)) - pow(y, 2) + 7 - (pow(z, 2) + pow(x, 6) - 18)\
			/(math.log1p(pow(x, 7) + abs(z) - 85) - pow(y, 5)) + ((math.tan(y) + y + 95)\
			/(abs(z) - pow(y, 4) + 94)))

print(f'{f11(100, -97, 80):.2e}')
print(f'{f11(4, -28, -99):.2e}')
