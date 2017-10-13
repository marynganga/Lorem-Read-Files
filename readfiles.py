#! /usr/bin/env python3

text_file = 'test.txt'

def read_file(text_file):
	"""
    Function that reads a text file and returns the data from the text file
	"""
	try:
		with open(text_file,'r') as handle:
			data = handle.read()
			return data
	except FileNotFoundError:
		return None

def read_words(text_file):
	'''
	Function that counts the number of times a word appears in a text file.
	'''
	with open(text_file,'r') as handle:
		data = handle.read()
		counter = 0
		for word in data.split():
			if word == "Python":
				counter += 1
		return counter	
		


def read_lines(text_file):
	'''
	Function that counts the number of lines in a text file.
	'''
	with open(text_file,'r') as handle:
		data = handle.readlines()
		counter2 = 0
		for line in data:
			counter2 += 1
		return counter2

def longest_word(text_file):
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
			# print(count)
			for word in data.split():
				if len(word) == count:
					return word
				
				

if __name__ == '__main__':
	read_file(text_file)
	read_words(text_file)
	read_lines(text_file)
	longest_word(text_file)