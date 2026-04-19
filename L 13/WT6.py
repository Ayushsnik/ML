from string import punctuation

import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression

from LR import features

data = pd.read_csv("Code6.csv")


def clean_function(text):
    text = text.lower()
    text = text.replace("'", "")
    text = word_tokenize(text)
    text = [x for x in text if x not in ["area", "bedrooms"]]
    text = [x for x in text if x not in punctuation]
    text = [x for x in text if x not in stopwords.words("english")]
    text = ",".join(text)
    return text

data["clean_info"] = data["info"].apply(clean_function)
print(data["clean_info"])


cv = CountVectorizer()
vector = cv.fit_transform(data["clean_info"])
print(vector)

feature = pd.DataFrame(vector.toarray())
