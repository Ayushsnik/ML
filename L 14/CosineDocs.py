import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

name1 = input("Enter the file name: ")
f= open(name1,"r")
s1 = f.read()
f.close()
print(s1)

name2 = input("Enter the file name: ")
f= open(name2,"r")
s2 = f.read()
f.close()
print(s2)


cv = CountVectorizer()
vectors = cv.fit_transform([s1, s2])

vector0 = vectors[0]
feature0 = pd.DataFrame(vector0.toarray(), columns=cv.get_feature_names_out())

vector1 = vectors[1]
feature1 = pd.DataFrame(vector1.toarray(), columns=cv.get_feature_names_out())

cs = cosine_similarity(vector0, vector1)
cs = cs.flatten()
print(cs*100)



