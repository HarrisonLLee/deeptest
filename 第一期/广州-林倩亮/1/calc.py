class Calc:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self):
		a = self.a + self.b
		return a
	def sub(self):
		s = self.a - self.b
		return s
	def mul(self):
		m = self.a * self.b
		return m
	def div(self):
		d = self.a / self.b
		return d
if __name__ == "__main__":
	a = 100
	b = 50
	count = Calc(a,b)
	print(count.add())
	print(count.sub())
	print(count.mul())
	print(count.div())
	
	