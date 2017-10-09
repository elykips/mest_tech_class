#there is another decorator build-in to python that operates on the class

class Apple():

	price=5

	def __init__(self,color):
		self.color = color
		self.price = Apple.price

	def __repr__(self):
		return """This is a {} cedi {} Apple""".format(self.price,self.color)

	#@staticmethod
	@classmethod
	def change_price(cls,new_price):
		cls.price = new_price

first = Apple("Red")
print(first)

second = Apple("Blue")
print(second)

third = Apple.change_price(6)

third = Apple("Green")
print(third)

print(first)


