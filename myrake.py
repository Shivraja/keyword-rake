# EXAMPLE ONE - SIMPLE
import rake
import operator
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 5, 3, 4)

# 2. run on RAKE on a given text
sample_file = open("test1.txt", 'r')
text = sample_file.read()

#keywords = rake_object.run(text)

# 3. print results
#print "Keywords:", keywords

print "----------"

# EXAMPLE TWO - BEHIND THE SCENES (from https://github.com/aneesha/RAKE/rake.py)

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

'''text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
       "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \
       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \
       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \
       "systems and systems of mixed types."
'''


'''
'''




# 1. Split text into sentences
sentenceList = rake.split_sentences(text)

#for sentence in sentenceList:
#    print "Sentence:", sentence

# generate candidate keywords
stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
#print "Phrases:", phraseList

# calculate individual word scores
wordscores = rake.calculate_word_scores(phraseList)

#mycode


myscore={};
for i in phraseList:
	myscore[i]=0;

for i in phraseList:
	myscore[i]+=1;

sorted_x = sorted(myscore.items(), key=operator.itemgetter(1),reverse=True);
print type(sorted_x)
#print sorted_x;
#for i in sorted_x:
#	print i[0]

#sorted_x=dict(sorted_x)
#print sorted_x

for i in sorted_x:
	#print i, sorted_x[i]
	#print i, sorted_x[i]
	word_List = rake.separate_words(i[0], 0)
	length1=len(word_List)
	if length1>1:
		print i[0],i[1];


# generate candidate keyword scores
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
#for candidate in keywordcandidates.keys():
#    print "Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate)

# sort candidates by score to determine top-scoring keywords
sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

# for example, you could just take the top third as the final keywords
#for keyword in sortedKeywords[0:(totalKeywords / 3)]:
#     print "Keyword: ", keyword[0], ", score: ", keyword[1]

#print rake_object.run(text)
