def f22(str):
	h = str & (0xC0000000)
	h >>= 1
	g = str & (0x3F000000)
	g >>= 1
	f = str & (0x800000)
	f >>= 10
	e = str & (0x700000)
	e >>= 6
	d = str & (0xFC000)
	d <<= 3
	c = str & (0x3FC0)
	c >>= 6
	b = str & (0x20)
	b <<= 26
	a = str & (0x1F)
	a <<= 8
	return hex(b | h | g | d | e | f | a | c)

print(f22(0xfbfb725b))
print(f22(0xb08c75ce))