import parser
import matrix_builder
import math
import global_vars

# stores the number of unique words in liberal and conservative articles
total_words = matrix_builder.num_words()

# stores the number of articles in the liberal and conservative files
num_lib_files = parser.line_count(global_vars.liberal_file)
num_con_files = parser.line_count(global_vars.conservative_file)

# stores the matrix of word counts from liberal and conservative articles
total_matrix = matrix_builder.matrix_builder(global_vars.liberal_file, global_vars.conservative_file, total_words)
cleaned_matrix = matrix_builder.clean_matrix(total_matrix, global_vars.neutral_file)
# builds an array of (count/num_words) fractions for each word in all the articles, where:
# count = total count of a word seen in all articles
# num_words = total number of words in that type of article


def build_vector(num_words, start_range, end_range):

	initial = [0 for i in range(total_words)]
	for word in range(total_words):
		count = 0
		for i in range(start_range, end_range):
			count += cleaned_matrix[i][word]
		if count == 0:
			initial[word] = 0
		else:
			initial[word] = math.log(count / float(num_words))
	return initial

# builds the arrays for both liberal and conservative articles 
lib_vec = build_vector(matrix_builder.num_lib_words(), 0, num_lib_files)
con_vec = build_vector(matrix_builder.num_con_words(), num_lib_files,num_lib_files + num_con_files)


def lib_vector():
	return lib_vec
def con_vector():
	return con_vec


#print lib_vec
#print con_vec
