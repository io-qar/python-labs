def f23(table):
	i = 0
	while i < len(table):
		j = 0
		while j < len(table):
			if i == j:
				j += 1
			elif table[i] == table[j]:
				del table[j]
				j -= 1
			else:
				j += 1
		i += 1

	for i in range(len(table)):
		table[i][0] = table[i][0][table[i][0].find(']') + 1:]
		table[i][1] = table[i][1][:table[i][1].find(' ')]
		table[i][2] = table[i][2].replace('.', '/')

	table = [[table[j][i] for j in range(len(table))] for i in range(len(table[0]))]

	return table

table = [
	['vaceslav28[at]gmail.com', 'Лезянц Вячеслав', '26.04.02'],
	['levamman56[at]gmail.com', 'Левамман Всеволод', '04.04.04'],
	['levamman56[at]gmail.com', 'Левамман Всеволод', '04.04.04'],
	['platon32[at]yandex.ru', 'Софук Платон', '18.11.03'],
	['qwqw[at]rambler.ru', 'Ронесский Антон', '22.04.04']
]

print(f23(table))
