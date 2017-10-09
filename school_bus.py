#school bus with 10 children and 1 driver
#buss cannot move untill there is a driver and 10 children
#make school bus and add 2 drivers and nine children
#what hapens?
class SchoolBus:

	def __init__(self, drivers=[], children=[]):
		self.drivers = drivers
		self.children = children

	def add_driver(self,driver):

		if isinstance(driver, Driver):
			self.drivers.append(driver)
		else:
			print("You are a child and cannot drive!")

	def add_child(self,child):
		if isinstance(child, Child):
			self.children.append(child)
		else:
			print("You are too old to be a child")

	def drive_bus(self):
		if len(self.drivers) <= 1 and len(self.children) >= 10:
			print("Bus can now drive")
		else:
			print("Bus cant be driven!")

class Person:

	def __init__(self, name):
		self.name = name

class Driver(Person):

	def __init__(self):
		pass

class Child(Person):

	def __init__(self):
		pass


	





