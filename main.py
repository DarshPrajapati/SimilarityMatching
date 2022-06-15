import string
import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
import math
import tensorflow as tf

#reading text file
def read_file(filename):

	try:
		with open(filename, 'r') as f:
			data = f.read()
		return data
	
	except IOError:
		print("Error opening or reading input file: ", filename)
		SystemExit
    
 #splitting using translation table
 translation_table = str.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_lowercase)

 #returns a list of the words
  def get_words_from_line_list(text):
	
	text = text.translate(translation_table)
	word_list = text.split()
	
	return word_list

#frequency of each word
def count_freq(word_list):
	
	D = {}
	
	for new_word in word_list:
		
		if new_word in D:
			D[new_word] = D[new_word] + 1
			
		else:
			D[new_word] = 1
			
	return D

#word frequnecy for each file
def word_frequencies_for_file(f):
	
	line_list = read_file(f)
	word_list = get_words_from_line_list(line_list)
	freq_mapping = count_freq(word_list)

	return freq_mapping

#dot product
def dotProduct(D1, D2):
	Sum = 0.0
	
	for key in D1:
		
		if key in D2:
			Sum += (D1[key] * D2[key])
			
	return Sum

#angle between 2 vectors
def vector_angle(D1, D2):
	n=dotProduct(D1, D2)
	d=math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
	
	return math.acos(n/d)

def docsimilarity(f1, f2):

	sorted_list_1 = word_frequencies_for_file(f1)
	sorted_list_2 = word_frequencies_for_file(f2)
	distance = vector_angle(sorted_list_1, sorted_list_2)
	
	print("Similarity score = %f (radians)"% distance)
  
#driver code
  docsimilarity("f1.txt", "f2.txt")
