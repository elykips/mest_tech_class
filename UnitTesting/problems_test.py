import problems
import unittest

class ValidAtmPinTest(unittest.TestCase):


	def test_if_1234_is_a_valid_pin(self):
		self.assertTrue(problems.is_valid('1234'))

	def test_if_12345_is_not_a_valid_pin(self):
		self.assertFalse(problems.is_valid('12345'))

	def test_if_a234_is_mnot_a_valid_pin(self):
		self.assertFalse(problems.is_valid('a234'))

class PalindromeTest(unittest.TestCase):


	def test_if_abbad_could_form_palindrom(self):
		self.assertTrue(problems.could_be_palindrome('abbad'))

	def test_if_sdsdfertr_could_form_palindrom(self):
		self.assertFalse(problems.could_be_palindrome('sdsdfertr'))

class RemoveVowels(unittest.TestCase):

	def test_to_remove_vowels_in_elkana(self):
		self.assertEqual(problems.remove_vowels("Elkana"),'lkn')

	def test_to_remove_vowels_in_Amaka(self):
		self.assertEqual(problems.remove_vowels("Amaka"), 'mk')

if __name__ =='__main__':
	unittest.main()