'''
steps
1) define function
2) verify if number of characters is 4 or 6
3) verify if the values are digits
4) Return False if condition holds 
5) Return True if condition holds

'''

def is_valid(pin):
	
	if len(pin) == 4 or len(pin) == 6:
		if pin.isdigit():
			return True
	return False

'''
Could a word be a palindrome problem:
steps
1) transform word to lowercase
2) create an empty dict of characters
3) create an empty list to track odd groups
4) loop through the word and collect characters and their counts
5) Insert the characters and their counts to the empty dict of characters
6) loop through the dictionary and collect characters with odd count
7) insert character with odd count to odd_group list
8) check if odd_group list count is <=1. if true then that word can be made a palindrom


insights for a palindrom:
 keep track of characters with odd count and ensure its <=1

'''

def could_be_palindrome(word):
	word = word.lower()
	characters = {}
	odd_group = []

	for character in word:
		if character in characters:
			characters[character] += 1
		else:
			characters[character] = 1

	print(characters)

	for character, count in characters.items():
		if count % 2 !=0:
			odd_group.append(character)
	return len(odd_group) <= 1

'''
Vowels Problem

Remove vowels in a string and replace with a consonant

1) create a list with vowels
3) loop through the given string while cheking if each of its characters are available on vowels list
4) delet character if available on vowels list
5) return list with remaining cgaracters



'''

def remove_vowels(my_string):

	my_string = my_string.lower()
	vowels = ['a','e','i','o','u']
	my_list = []
	for consonant in my_string:
		if consonant not in vowels:
			my_list.append(consonant)
	return "".join(my_list)