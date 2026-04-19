import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

s1 = "hello world"
s2 = "HELLO WORLD"

cv = CountVectorizer()
vectors = cv.fit_transform([s1, s2])

vector0 = vectors[0]
feature0 = pd.DataFrame(vector0.toarray(), columns=cv.get_feature_names_out())
print(feature0)

vector1 = vectors[1]
feature1 = pd.DataFrame(vector1.toarray(), columns=cv.get_feature_names_out())
print(feature1)


cs = cosine_similarity(vector0, vector1)
cs = cs.flatten()
print(cs*100)




