import parser
import global_vars

total_liberal_words = 0
total_conservative_words = 0
unique_liberal_words = 0
unique_conservative_words = 0
unique_joint_words = 0
lib_dict = {}
cons_dict = {}
joint_dict = {}
ordering_dict = {}


# Update the liberal dictionary and relevant globals
def update_liberal_dict():
	global lib_dict
	global total_liberal_words
	global unique_liberal_words
	lib_dict = parser.build_dict(global_vars.liberal_file)
	total_liberal_words = sum(lib_dict.values())
	unique_liberal_words = len(lib_dict.keys())
	return lib_dict
#Update the conservatve dictionary and relevant globals.
def update_conservative_dict():
	global cons_dict
	global total_conservative_words
	global unique_conservative_words
	cons_dict = parser.build_dict(global_vars.conservative_file)
	total_conservative_words = total_conservative_words = sum(cons_dict.values())
	unique_conservative_words = len(cons_dict.keys())
	return cons_dict

#Update the joint dictionary
def update_joint_dict():
	global joint_dict
	joint_dict = parser.combine_dict(lib_dict, cons_dict)
	return joint_dict

#Update global with the unique words
def update_unique_joint_words():
	global unique_joint_words
	unique_joint_words = len(joint_dict.keys())
	return unique_joint_words

#Update the ordering dictionary, which gives each unique word a unique key.
def update_ordering_dict():
	#print joint_dict
	global ordering_dict
	ordering_dict = parser.create_ordering(joint_dict)
	return ordering_dict


# cleans a matrix for most common words
def clean_matrix(matrix, filename):
	common_words = open(filename, 'r')
	for word in common_words:
		if word in joint_dict:
			for article in matrix:
				article[ordering_dict[word]] = 0
	return matrix
				
# these next 3 functions return values needed in other files 
def num_words():
	return unique_joint_words

def num_lib_words():
	return unique_liberal_words

def num_con_words():
	return unique_conservative_words

#builds list from a specific article and total number of words
def list_builder(article, total_words):	
	word_dict = parser.parse_page(article,{})
	word_array = [0 for i in range(total_words)]
	#print word_dict
	#print ordering_dict
	for key in word_dict:
		if key in joint_dict:
			word_array[ordering_dict[key]] = word_dict[key]
	#num_words = sum(word_array)
	#word_array = [item / float(num_words) for item in word_array]
	return word_array

#reads conservative and liberal files and builds matrix from individual lists
def matrix_builder(lib_file, cons_file, total_words):
	#print "mat_builder called"
	larticles = open(lib_file, 'r')
	carticles = open(cons_file, 'r')
	init_list = []
	for line in larticles:
		init_list.append(list_builder(line, total_words))
	for line in carticles:
		init_list.append(list_builder(line, total_words))
	return init_list

