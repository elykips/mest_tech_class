class Person:

	def __init__(self, compalint="No water, too much PHP"):
		self.__complaint = compalint

	def complaint(self):
		print(self.__complaint)

class Eit(Person):
		pass

class Fellow(Person):
		pass

class Cat:
	pass

people = list()
people.append(Fellow())

for _ in range(27):
	people.append(Eit())
people.append(Cat())

andrew = Fellow()
fisi = Eit()

for person in people:
	if isinstance(person,Person):
		person.complaint()
	else:
		print("Not a Person")
