class GFG:
	def __init__(self, name, company):
		self.name = name
		self.company = company

	def show(self):
		print("Hello my name is " + self.name+" and I" +
			" work in "+self.company+".")


obj = GFG("Gopi", "Y2k")
obj.show()
