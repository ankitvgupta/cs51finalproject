import parser
import matrix_builder
import vector_builder
import numpy

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
	if lib_prob/con_prob > 1:
		return "Liberal"
	if con_prob/lib_prob < 1:
		return "Conservative"
	else:
		return "Inconclusive"

def prepare_array(url):
	return matrix_builder.list_builder(url, matrix_builder.num_words())


def parse_test_cases(inputfile):
	test_cases = open(inputfile, 'r')
	for line in test_cases:
		pol_party = check_case(prepare_array(line))
		print line, pol_party

parse_test_cases('testcases.txt')


