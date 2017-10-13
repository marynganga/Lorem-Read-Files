import unittest
import readfiles

class TestReadFiles(unittest.TestCase):
	'''
	Class to test the functions on the read files modules

	Args:
		unittest.TestCase: Class from unittest module to create unittests.
	'''

	def test_get_data(self):
		"""
		Test case to confirm that we are getting data from the file
		"""
		with open('test.txt','r') as handle:
			data = handle.read()
			self.assertEqual(data,readfiles.read_file('test.txt'))	

	def test_nonfile(self):
		"""
		Test to confirm that an exeption is raised when a wrong file is inputted
		"""
		self.assertEqual(None,readfiles.read_file('tests.txt'))

	def test_word_count(self):
		'''
		Test to confirm that we are getting the right number of words
		'''
		with open('test.txt','r') as handle:
			data = handle.read()
			counter = 0
			for word in data.split():
				word == "Python"
				counter += 1
				return counter
			self.assertEqual(counter,readfiles.read_words('test.txt'))



	def test_line_count(self):
		'''
		Test to confirm the number of lines in a text file
		'''
		with open('test.txt','r') as handle:
			data = handle.readlines()
			counter2 = 0
			for line in data:
				counter2 += 1
				return counter2
			self.assertEqual(counter2,readfiles.read_lines('test.txt'))

	def test_longest_word(self):
		'''
		Test to confirm the longest word in a text file
		'''
		with open('test.txt','r') as handle:
			data = handle.read()
			data = data.replace(',','')
			data = data.replace('.','')
			count = 0
			for word in data.split():
				if len(word) > count:

					count = len(word)
			for word in data.split():
				if len(word) == count:
					return word
			self.assertEqual(word,readfiles.longest_word('test.txt'))
				
		
		
if __name__ == '__main__':
	unittest.main(verbosity=2)	