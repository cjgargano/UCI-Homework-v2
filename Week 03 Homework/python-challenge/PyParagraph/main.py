import re

#Read in data file
file = open("raw_data/paragraph_test.txt")
text = file.read()

words = re.sub("[.!?,-;()']", " ", text).split()
words2 = text.split()

print(" ")
print(text)
print(" ")
print(" ")
print("--------------------")

print(" ")
print(words)
print(" ")
print(" ")
print("--------------------")

#Find the word count
word_count = len(words)

#Declare variables
sentence_count = 0
letter_count = 0

#Find number of sentences by looking at count of puncuation marks in 'words2' list
for w in words2:
	if w.endswith(".") or w.endswith("?") or w.endswith("!"):
		sentence_count += 1

#Find letter count using 'words' list; add len(w) to variable and average after the loop ends
for w in words:
	letter_count += len(w)

########## Output ##########
print(" ")
print("Paragraph Analysis")
print("--------------------")

print("Approximate Word Count:      " + str(word_count))
print("Approximate Sentence Count:  " + str(sentence_count))
print("Approximate Word Length:     " + str(round(letter_count / word_count,2)) + " letters per word")
print("Approximate Sentence Length: " + str(round(word_count / sentence_count,2)) + " words per sentence")
