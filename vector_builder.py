import parser
import matrix_builder
import math
import global_vars



#Builds the vector of word frequencies from the matrix of word frequencies
def build_vector(num_words, start_range, end_range):
	total_words = matrix_builder.num_words()
	total_matrix = matrix_builder.matrix_builder(global_vars.liberal_file, global_vars.conservative_file, total_words)
	cleaned_matrix = matrix_builder.clean_matrix(total_matrix, global_vars.neutral_file)

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

#Find the liberal and conservative vectors by using build_vector
def lib_vector():
	num_lib_files = parser.line_count(global_vars.liberal_file)
	return build_vector(matrix_builder.num_lib_words(), 0, num_lib_files)
def con_vector():
	num_lib_files = parser.line_count(global_vars.liberal_file)
	num_con_files = parser.line_count(global_vars.conservative_file)
	return build_vector(matrix_builder.num_con_words(), num_lib_files,num_lib_files + num_con_files)


