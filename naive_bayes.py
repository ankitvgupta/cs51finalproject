import checkdoc
import global_vars
import cross_validate
import web_crawl
import sys

#Standard Naive Bayes with Test cases in the testcases.txt file
def version1():
	print "\n\n\nBeginning Version 1 - Standard Naive-Bayes, with test cases in the testcases.txt file.\nSome of these steps may take one or more minutes.\n\n\n"
	checkdoc.parse_test_cases(global_vars.test_file)

#Beginnig
def version2():
	print "\n\n\nBeginning Version 2 - Standard Naive-Bayes, with test cases found by crawling the site in the global_vars.py file.\nSome of these steps may take one or more minutes.\n\n\n"
	web_crawl.run_tests()

def version3():
	print "\n\n\nBeginning Version 3 - Cross-Validation\nSome of these steps may take one or more minutes.\n\n\n"
	cross_validate.validate()


counter = -1
if len(sys.argv) == 1:
	version1()
	version2()
	version3()
elif len(sys.argv) != 4:
	print "Usage: need to give three arguments"
else:
	for i in sys.argv:
		counter += 1
		if counter == 1 and i == '1':
			version1()
			
		if counter == 2 and i == '1':
			version2()
			
		if counter == 3 and i == '1':
			version3()
		







