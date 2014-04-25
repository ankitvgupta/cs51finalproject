import parser

#create dictionary with words from each file
liberal_dict = parser.build_dict('liberal.txt')
conservative_dict = parser.build_dict('conservative.txt')

#total words in each class of articles
total_liberal_words = sum(liberal_dict.values())
total_conservative_words = sum(conservative_dict.values())

#number of unique words in each class of articles
unique_liberal_words = len(liberal_dict.keys())
unique_conservative_words = len(conservative_dict.keys())

#frequency dictionaries for each class of articles
liberal_freq_dict = parser.divide_dict(liberal_dict, total_liberal_words)
conservative_freq_dict = parser.divide_dict(conservative_dict, total_conservative_words)

#dictionary with all articles from both classes
joint_dict = parser.combine_dict(liberal_dict, conservative_dict)
unique_joint_words = len(joint_dict.keys())

#assigns unique index to each unique word
ordering_dict = parser.create_ordering(joint_dict)

