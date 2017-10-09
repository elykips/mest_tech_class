#static methods
import random

class StringHelper:

	@staticmethod
	def randomCase(string):
		tempstr = ""
		for char in string:
			tempstr += char.upper() if random.randint(0,1) else char.lower()

		return tempstr
text = "Hello this is a text"
print(StringHelper.randomCase(text))