from nltk import word_tokenize
s1 = "I love@coding and_ML#Python"
s2 = word_tokenize(s1)
print(s2)

s3 = "I is@a #letter"
s4 = s3.split(" ")
print(s4)