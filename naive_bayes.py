import checkdoc
import global_vars
import cross_validate

#global_vars.init()

checkdoc.parse_test_cases(global_vars.test_file)
print global_vars.neutral_file
cross_validate.change_global()

print global_vars.neutral_file


