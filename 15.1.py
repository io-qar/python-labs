def f21(x):
	if x[1] == 1969:
		if x[3] == 'cson':
			if x[0] == 'bison':
				return 0
			elif x[0] == 'java':
				if x[4] == 'dylan':
					return 1
				elif x[4] == 'stata':
					return 2
				elif x[4] == 'elm':
					return 3
			elif x[0] == 'glyph':
				if x[2] == 'eq':
					return 4
				if x[2] == 'asn.1':
					return 5
		elif x[3] == 'krl':
			if x[0] == 'bison':
				if x[4] == 'dylan':
					return 6
				elif x[4] == 'stata':
					return 7
				elif x[4] == 'elm':
					return 8
			elif x[0] == 'java':
				return 9
			elif x[0] == 'glyph':
				return 10
	elif x[1] == 1971:
		return 11

x = ['bison', 1969, 'asn.1', 'krl', 'stata']
print(f21(x))