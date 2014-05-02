import matrix_builder
import vector_builder
import numpy

lib_vector = []
con_vector = []

#Update the liberal and conservative vectors
def update_vectors():
	global lib_vector
	global con_vector
	lib_vector = vector_builder.lib_vector()
	con_vector = vector_builder.con_vector()

#Implements the dot product of two vectors represented as arrays using Numpy
def dot_arrays(arr1, arr2):
	numpy_arr1 = numpy.array(arr1)
	numpy_arr2 = numpy.array(arr2)
	numpy_dotted = numpy.dot(numpy_arr1, numpy_arr2)
	return numpy_dotted.tolist()

#Check if a certain article is liberal, conservative, or inconclusive
def check_case(arr):
	lib_prob = dot_arrays(lib_vector, arr)
	con_prob = dot_arrays(con_vector, arr)

	if con_prob == 0.0:
		return "Inconclusive"
	elif lib_prob/con_prob > 1.05:
		return "Liberal"
	elif con_prob/lib_prob > 1.05:
		return "Conservative"
	else:
		return "Inconclusive"

#Make the array of words for a certain url
def prepare_array(url):
	return matrix_builder.list_builder(url, matrix_builder.num_words())

#get all of the test cases from an input file, update all of the globals, and then find the ratio.
def parse_test_cases(inputfile):
	print "    Step 1: Constructing Liberal Word dictionary..."
	matrix_builder.update_liberal_dict()
	print "    Step 2: Constructing Conservative Word dictionary...."
	matrix_builder.update_conservative_dict()
	#matrix_builder.update_liberal_freq_dict()
	#matrix_builder.update_conservative_freq_dict()
	print "    Step 3: Constructing joint dictionary..."
	matrix_builder.update_joint_dict()
	print "    Step 4: Finding unique joint words..."
	matrix_builder.update_unique_joint_words()
	print "    Step 5: Constructing ordering dictionary..."
	matrix_builder.update_ordering_dict()
	print "    Step 6: Updating word vectors..."
	update_vectors()
	print "    Step 7: Calculating success rates...\n"

	liberals = 0
	conservatives = 0
	inconclusives = 0

	test_cases = open(inputfile, 'r')
	for line in test_cases:
		#print line
		try:
			pol_party = check_case(prepare_array(line))
			if pol_party == "Liberal":
				liberals += 1
			elif pol_party == "Conservative":
				conservatives += 1
			elif pol_party == "Inconclusive":
				inconclusives += 1
		except:
			continue
		#print line, pol_party
		#print "\n\n\n\n\n\n\n\n"
	lib_ratio = (liberals)/ float((liberals + conservatives + inconclusives)) * 100
	cons_ratio = (conservatives)/ float((liberals + conservatives + inconclusives)) * 100
	inc_ratio = (inconclusives)/ float((liberals + conservatives + inconclusives)) * 100
	str_lib = str(lib_ratio) + " percent of articles were liberal, \n" 
	str_cons = str(cons_ratio) + " percent of articles were conservative, and\n "
	str_inc = str(inc_ratio) + " percent of articles were incoclusive."
	print str_lib + str_cons + str_inc 

#Get the average of an array
def array_average(arr):
	return float(sum(arr))/float(len(arr))

# The same as parse_test_cases except with more functionality for cross-validation
# the first num of them will be liberal ones
def validator_parse_test_cases(inputfile, num):
	val_test_cases = open(inputfile, 'r')
	val_test_counter = -1
	lib_results = []
	con_results = []

	for line in val_test_cases:
		#print "    " + line
		val_test_counter += 1

		party = check_case(prepare_array(line))
		if val_test_counter < num and party == "Conservative":
			lib_results.append(0)
		elif val_test_counter < num and party == "Liberal":
			lib_results.append(1)
		elif val_test_counter < num:
			lib_results.append(1)
		elif val_test_counter >= num and party == "Conservative":
			con_results.append(1)
		elif val_test_counter >= num and party == "Liberal":
			con_results.append(0)
		elif val_test_counter >= num:
			con_results.append(1)
	return [array_average(lib_results), array_average(con_results)]



