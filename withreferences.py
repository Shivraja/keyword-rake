# EXAMPLE ONE - SIMPLE
import rake
import operator
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 5, 3, 4)

# 2. run on RAKE on a given text
sample_file = open("test6.txt", 'r')
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

flag=False
reftext=text.split(' ')
#for x in
#print text

sentence=" ";
for x in reftext:
#	print x
	if(flag==True):
		sentence=sentence +" "+x
	if "EFERENCES" in x: 
		flag=True

referencesentencelist=rake.split_sentences(sentence)
stopwordpattern = rake.build_stop_word_regex(stoppath)
refphraseList = rake.generate_candidate_keywords(referencesentencelist, stopwordpattern)

#print sentence

'''
'''




# 1. Split text into sentences
sentenceList = rake.split_sentences(text)

#for sentence in sentenceList:
#    print "Sentence:", sentence

# generate candidate keywords
#stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
#print "Phrases:", phraseList

# calculate individual word scores
wordscores = rake.calculate_word_scores(phraseList)

#mycode


myscore={};
for i in phraseList:
	myscore[i]=0;

for i in phraseList:
	if "IEEE" not in i and "ieee" not in i:
		myscore[i]+=1;

for i in refphraseList:
	if "IEEE" not in i and "ieee" not in i:
		myscore[i]+=1

'''
for i in phraseList:
#	valid[i]=1;
	for j in phraseList:
		word_List = rake.separate_words(j, 0)
		length1=len(word_List)
		if myscore[i]==-1 or length1<2:
			continue
		if j in i:
			myscore[i]=max(myscore[i],myscore[j])
			myscore[j]=-1
'''

sorted_x = sorted(myscore.items(), key=operator.itemgetter(1),reverse=True);
#print type(sorted_x)
#print sorted_x;
#for i in sorted_x:
#	print i[0]

#sorted_x=dict(sorted_x)
#print sorted_x

newsorted={}

j=0
for i in sorted_x:
	word_List = rake.separate_words(i[0], 0)
	length1=len(word_List)
	if j==50:
		break
	if length1>1:
		newsorted[j]=i[0]
		j+=1		



count=0
valid={}
for i in newsorted:
	valid[i]=0
	continue
l=0
for i in newsorted:
	word_List=rake.separate_words(newsorted[i],0)
	length1=len(word_List)

	if valid[i]==-1:
		continue
	
	for k in newsorted:
		l=0
		for j in word_List:
			if i==k:
				continue
			if valid[k]==-1:
				continue

			if j in newsorted[k]:
				l+=1
			if l>=2:
				#print newsorted[i]+"     "+newsorted[k]
				length2=len(rake.separate_words(newsorted[k],0))
				if length1>=length2:
					valid[k]=-1
				#	print "----------->  "+newsorted[k]
				#	print "Hi"


for i in newsorted:
	pass
	#print newsorted[i]+" "+str(valid[i])
count=0
for i in newsorted:
	if valid[i]!=-1:
		print newsorted[i]
		count+=1
	if count==20:
		break
count=0
for i in sorted_x:
	#print i, sorted_x[i]
	#print i, sorted_x[i]
	word_List = rake.separate_words(i[0], 0)
	length1=len(word_List)
	if length1>1:
	#	print i[0]
		count+=1
	if count==20:
		break


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