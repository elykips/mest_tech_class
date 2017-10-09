#add static method calld abbreviate
#takes a string and number of characters

class Sentence:

	@staticmethod
	def abbreviate(string,num):
		if num < len(string):
			return string[0:num]+"..."
		else:
			return string[0:num]

my_string = "python is awesome"
print(Sentence.abbreviate(my_string,1000))