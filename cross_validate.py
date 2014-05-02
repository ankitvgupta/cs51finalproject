#import parser
import global_vars
import checkdoc
import matrix_builder


#Reset all of the validator files
def clear_validator_files():
	open(global_vars.validator_lib, 'w').close()
	open(global_vars.validator_cons, 'w').close()
	open(global_vars.validator_totest, 'w').close()

#Add to the validator files given a certain range
def add_validator_files(start_range, end_range):
	lib_counter = -1
	cons_counter = -1
	totest_counter = -1


	lib_file = open(global_vars.orig_liberal_file, 'r')
	cons_file = open(global_vars.orig_conservative_file, 'r')
	v_lib = open(global_vars.validator_lib, 'w')
	v_cons = open(global_vars.validator_cons, 'w')
	v_totest = open(global_vars.validator_totest, 'w')


	for line in lib_file:
		lib_counter += 1
		if lib_counter < start_range or lib_counter >= end_range:
			v_lib.write(line)
		else:
			v_totest.write(line)
	for line in cons_file:
		cons_counter += 1
		if cons_counter < start_range or cons_counter >= end_range:
			v_cons.write(line)
		else:
			v_totest.write(line)
	v_lib.close()
	v_cons.close()
	v_totest.close()


#returns the number of each type of article we have
def find_num_articles():
	lib_file = open(global_vars.orig_liberal_file, 'r')
	counter = 0
	for line in lib_file:
		counter += 1
	return counter

#Update all of the global variables for each validation set and call the necessary validation sets
def validate():
	#make the liberal and conservative files be the validator ones
	global_vars.liberal_file = global_vars.validator_lib
	global_vars.conservative_file = global_vars.validator_cons

	global num_articles
	num_articles = find_num_articles()
	size_of_check = num_articles / 10

	
	for i in range(0, num_articles, size_of_check):


		print "Validation set " + str((i / size_of_check) + 1)
		print "    Step 1: Resetting files for next run..."
		clear_validator_files()
		add_validator_files(i, i+size_of_check)


		print "    Step 2: Constructing Liberal Word dictionary..."
		matrix_builder.update_liberal_dict()


		print "    Step 3: Constructing Conservative Word dictionary...."
		matrix_builder.update_conservative_dict()

		print "    Step 4: Constructing joint dictionary..."
		matrix_builder.update_joint_dict()


		print "    Step 5: Finding unique joint words..."
		matrix_builder.update_unique_joint_words()


		print "    Step 6: Constructing ordering dictionary..."
		matrix_builder.update_ordering_dict()


		print "    Step 7: Updating word vectors..."
		checkdoc.update_vectors()


		print "    Step 8: Calculating success rates...\n"
		result = checkdoc.validator_parse_test_cases(global_vars.validator_totest, size_of_check)

		print "    " + str(result[0] * 100) + " percent of liberal articles were correct, and " + str(result[1] * 100) + " percent of conservative articles were correct.\n\n"





