import parser
import global_vars

#create dictionary with words from each file
liberal_dict = parser.build_dict(global_vars.liberal_file)
conservative_dict = parser.build_dict(global_vars.conservative_file)

#total words in each class of articles
total_liberal_words = sum(liberal_dict.values())
total_conservative_words = sum(conservative_dict.values())

#number of unique words in each class of articles
unique_liberal_words = len(liberal_dict.keys())
unique_conservative_words = len(conservative_dict.keys())

#frequency dictionaries for each class of articles
liberal_freq_dict = parser.divide_dict(liberal_dict, total_liberal_words)
conservative_freq_dict = parser.divide_dict(conservative_dict, total_conservative_words)

#dictionary with all articles from both classes
joint_dict = parser.combine_dict(liberal_dict, conservative_dict)
unique_joint_words = len(joint_dict.keys())

#assigns unique index to each unique word
ordering_dict = parser.create_ordering(joint_dict)

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
	for key in word_dict:
		if key in joint_dict:
			word_array[ordering_dict[key]] = word_dict[key]
	#num_words = sum(word_array)
	#word_array = [item / float(num_words) for item in word_array]
	return word_array

#reads conservative and liberal files and builds matrix from individual lists
def matrix_builder(lib_file, cons_file, total_words):
	print "mat_builder called"
	larticles = open(lib_file, 'r')
	carticles = open(cons_file, 'r')
	init_list = []
	for line in larticles:
		init_list.append(list_builder(line, total_words))
	for line in carticles:
		init_list.append(list_builder(line, total_words))
	return init_list

