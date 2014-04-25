import parser
import matrix_builder

total_words = matrix_builder.num_words()
num_lib_files = parser.line_count('liberal.txt')
num_con_files = parser.line_count('conservative.txt')

total_matrix = matrix_builder.matrix_builder('liberal.txt', 'conservative.txt', total_words)

def build_vector(num_words, start_range, end_range):
	initial = [0 for i in range(total_words)]
	for word in range(total_words):
		count = 0
		for i in range(start_range, end_range):
			count += total_matrix[i][word]
		initial[word] = count / float(num_words)
	return initial

lib_vec = build_vector(matrix_builder.num_lib_words(), 0, num_lib_files)
con_vec = build_vector(matrix_builder.num_con_words(), num_lib_files,num_lib_files + num_con_files)

print lib_vec
print con_vec
