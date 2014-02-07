
def listofwords(*user_words):
	lst = []
	for i in user_words:
		lst.append(i)
		print lst
	return lst

	print "I love " + lst[0] + ", I hate " + lst[1]

print "I love _____, I hate _____, I want to _____"
words = raw_input("Pick 3 words?: ").split(",")
listofwords(words)

#update story with inputted words
#print out story with words.

