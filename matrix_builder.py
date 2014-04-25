import parser


liberal_dict = parser.build_dict('liberal.txt')
conservative_dict = parser.build_dict('conservative.txt')

total_lib_words = sum(liberal_dict.values())
total_conservative_words = sum(conservative_dict.values())

unique_lib_words = len(liberal_dict.keys())
unique_conservative_words = len(conservative_dict.keys())

liberal_freq_dict = parser.divide_dict(liberal_dict, total_lib_words)
conservative_freq_dict = parser.divide_dict(conservative_dict, total_conservative_words)


joint_dict = parser.combine_dict(liberal_dict, conservative_dict)
unique_joint_words = len(joint_dict.keys())

ordering_dict = parser.create_ordering(joint_dict)

print len(ordering_dict.keys())
print joint_dict

