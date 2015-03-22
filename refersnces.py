sample_file = open("test1.txt", 'r')
text = sample_file.read()
#text="Hi I am Pradeep REFERENCES is here"
flag=False
newtext=text.split(' ')
#for x in
#print text
sentence=" ";
for x in newtext:
#	print x
	if "REFERENCES" in x: 
		flag=True
	if(flag==True):
		sentence=sentence +" "+x

print sentence