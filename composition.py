#class containing instances of other classes
#instances of super class can access instances of chilren classes

class Egg:

	def __init__(self, color, is_broken="False"):
		self.color = color
		self.__is_broken = is_broken

	def __repr__(self):
		return self.color

	def drop(self):
		self.__is_broken = True

class EggCarton:

	def __init__(self):
		self.crate = list()

	def get_crate(self):
		return self.crate

	def add_egg(self, egg):
		self.crate.append(egg)

	def drop_egg(self):
		last_egg = self.crate.pop()
		last_egg.drop()

if __name__ == "__main__":
	carton = EggCarton()
	my_egg = Egg("blue")
	for _ in range(3):
		carton.add_egg(my_egg)
	print(carton.get_crate())

	for _ in range(4):
		carton.add_egg(my_egg)
	print(carton.get_crate())

	for _ in range(2):
		carton.add_egg(my_egg)
	print(carton.get_crate())

	carton.drop_egg()
	print(carton.last_egg)