class C32:
	def __init__(self):
		self.position = 'A'

	def solve(self, dict_solve):
		for pos, key in dict_solve.items():
			if self.position == pos:
				self.position = key[0]
				return key[1]
		return None

	def order(self):
		return self.solve({
			# current position: [next position, return]
			'A': ['B', 0],
			'B': ['C', 1],
			'D': ['E', 4],
			'E': ['C', 7]
		})

	def clear(self):
		return self.solve({
			'B': ['E', 2],
			'E': ['F', 6],
			'D': ['F', 5],
			'F': ['A', 8],
			'C': ['D', 3]
		})

o = C32()
print(o.order())
print(o.clear())
print(o.order())
print(o.clear())
print(o.clear())
print(o.clear())
print(o.order())
print(o.order())
print(o.clear())
print(o.order())
print(o.clear())
print(o.order())
print(o.clear())

print(o.order())
print(o.clear())
print(o.clear())
print(o.clear())
print(o.order())
print(o.order())
print(o.clear())
print(o.order())
print(o.order())
print(o.clear())
print(o.clear())
print(o.clear())