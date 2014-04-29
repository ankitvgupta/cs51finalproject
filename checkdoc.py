import parser
import matrix_builder
import vector_builder
import numpy

lib_vector = []
con_vector = []

def update_vectors():
	global lib_vector
	global con_vector
	lib_vector = vector_builder.lib_vector()
	con_vector = vector_builder.con_vector()

def dot_arrays(arr1, arr2):
	numpy_arr1 = numpy.array(arr1)
	numpy_arr2 = numpy.array(arr2)
	numpy_dotted = numpy.dot(numpy_arr1, numpy_arr2)
	return numpy_dotted.tolist()

def check_case(arr):
	lib_prob = dot_arrays(lib_vector, arr)
	con_prob = dot_arrays(con_vector, arr)
	print lib_prob
	print con_prob

	if lib_prob/con_prob > 1.0:
		return "Liberal"
	elif con_prob/lib_prob > 1.0:
		return "Conservative"
	else:
		return "Inconclusive"

def prepare_array(url):
	return matrix_builder.list_builder(url, matrix_builder.num_words())


def parse_test_cases(inputfile):
	matrix_builder.update_liberal_dict()
	matrix_builder.update_conservative_dict()
	#matrix_builder.update_liberal_freq_dict()
	#matrix_builder.update_conservative_freq_dict()
	matrix_builder.update_joint_dict()
	matrix_builder.update_unique_joint_words()
	matrix_builder.update_ordering_dict()
	update_vectors()

	test_cases = open(inputfile, 'r')
	for line in test_cases:
		pol_party = check_case(prepare_array(line))
		print line, pol_party

def array_average(arr):
	return float(sum(arr))/float(len(arr))

#the first num of them will be liberal ones
def validator_parse_test_cases(inputfile, num):
	val_test_cases = open(inputfile, 'r')
	val_test_counter = -1
	lib_results = []
	con_results = []

	for line in val_test_cases:
		
		val_test_counter += 1

		party = check_case(prepare_array(line))
		if val_test_counter < num and party == "Conservative":
			lib_results.append(0)
		elif val_test_counter < num and party == "Liberal":
			lib_results.append(1)
		elif val_test_counter >= num and party == "Conservative":
			con_results.append(1)
		elif val_test_counter >= num and party == "Liberal":
			con_results.append(0)
	return [array_average(lib_results), array_average(con_results)]



