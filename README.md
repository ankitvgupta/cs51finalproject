Naive Bayes: Examining the Partisanship of Online Content
Ankit Gupta, Emily Wang, Nishant Kakar, and Hirsh Jain
Computer Science 51 - Harvard University

In this file, there are a set of instructions to let you know how to best use this software. First, I will list a few warnings. Then, I will list some of the general features that this software accomplishes. Last, I will explain how to correctly provide input to the software. 


A few warnings:
1) DO NOT modify validate_lib.txt, validate_cons.txt, and validate_totest.txt in the files folder. Our code is very file dependent, and these files are often read and written to automatically by the code. However, NO input or output are every provided to or from these files. 
2) Only ever run the naive_bayes.py file, with the correct inputs as given below.
3) Not all websites are good for the web-crawler to start on. Some websites do not have enough links to get the critical mass of 100 articles. If you wish to change the website that the crawler starts on (see below), try to pick a website that has lots of links in the article itself (most CNN articles have this feature). Also, use the article we provide as an example.
4) DO NOT change any of the global variables in global_vars.py, except the url_to_crawl one, as explained below.
5) You MUST have Python 2.7.5 for this to work. Some of our group members with Python 2.7.2 had to upgrade to get the code to work, and it is not designed to be compatible with higher versions of python. However, this seemed to be the most widely used version of Python, so we don't think it'll be much of a problem. If you have any trouble running the code because of these compatability issues, please let us know - we will be happy to demonstrate the code on our own computers if you wish.



Features:
This software hss a ton of features, and it can be modified to accept input in a variety of ways. First, the main functionality of our software is to use the naive bayes method to determine whether a given article appears to hbe more conservative or liberal. To do this, we first train the software on a set of 100 conservative and 100 liberal files - this takes a ton of time, and that is just a result of the fact that each of the articles are long and it takes a long time to parse and make sense of them. Then, with these trained files, we can do a number of things. One, we can supply a list of articles that the software will categorize as either liberal or conservative, and then print at the end the number that were liberal, conservative, and inconclusive. Second, we can give an input file, and the software will crawl the webpage that it is on and find similar pages (so a cnn article will find other cnn articles), and then determine whether the site as a whole leans one way or the other. Lastly, we have 10-fold cross-validation, meaning that we train on a subset of our training set, and classify the remaining articles to determine the accuracy of our trainer. So, we can summarize these with three key functions:

1) Version 1 - Naive Bayes with files to classify in files/testcases.txt
2) Version 2 - Naive Bayes with files to classify found by crawling the website specified in global_vars.py
3) Version 3 - Naive Bayes with Cross-Validation on the training set


Instructions:
Navigate to the code directory in the terminal, and type "python naive_bayes.py" to run all three versions in order. Otherwise, navugate to the code directory in the terminal and type "python naive_bayes.py x_1 x_2 x_3", where each of x_i are either 1 or 0, specifying whether to run version i. In other words, to run Versions 1 and 3, type "python naive_bayes.py 1 0 1".

Now, for case-by-case instructions when running each version
Version 1) Put the files that you want to classify in files/testcases.txt. The classifier will train on the files in files/liberal.txt and files/conservative.txt. We would NOT recommend changes these two files since we picked each article, but you may if you wish.
Version 2) Put the article that you want to begin the web-crawler on as the value of the variable url_to_crawl in global_vars.py. We recommend that you pick an article with a lot of links, or else it won't work. It would be best if you just used the one that is provided since we know that one will work.
Version 3) No extra steps needed - just do not change any of the text files in the files folder that begin with 'validate' - those will get modified by the code. 


