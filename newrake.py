# EXAMPLE ONE - SIMPLE
import rake
import operator
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 5, 3, 4)

# 2. run on RAKE on a given text
sample_file = open("test.txt", 'r')
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
for i in keywords:
	print "Keywords:", i

print "----------"
raw_input()
