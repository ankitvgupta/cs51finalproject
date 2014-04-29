import parser
import global_vars
import checkdoc

def clear_validator_files():
	open(global_vars.validator_lib, 'w').close()
	open(global_vars.validator_cons, 'w').close()
	open(global_vars.validator_totest, 'w').close()

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
	lib_file = open(global_vars.liberal_file, 'r')
	counter = 0
	for line in lib_file:
		counter += 1
	return counter

def validate():
	#make the liberal and conservative files be the validator ones
	global_vars.liberal_file = global_vars.validator_lib
	global_vars.conservative_file = global_vars.validator_cons

	global num_articles
	num_articles = find_num_articles()

	
	size_of_check = num_articles / 10
	for i in range(0, num_articles - size_of_check, size_of_check):
		clear_validator_files()
		add_validator_files(i, i+size_of_check)
		result = checkdoc.validator_parse_test_cases(global_vars.validator_totest, size_of_check)
		print result[0], result[1] 





