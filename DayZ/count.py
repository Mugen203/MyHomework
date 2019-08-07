import re
#number of words

random_file = open("randomtxt.txt").read()
words = random_file.split()

print(len(words))

#To search for occurence of a particular word
occurence = re.findall("Over", random_file)

print(len(occurence))

