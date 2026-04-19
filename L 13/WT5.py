from string import punctuation

import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code5.csv")


def clean_function(text):
    text=text.lower()

    text = word_tokenize(text)#ye split jaisa hi hai but split ka drwback ko overcome krta hai
    text=[x for x in text if x not in ["area","bedrooms"]]
    text=[x for x in text if x not in punctuation]
    text=[x for x in text if x not in stopwords.words("english")]# ye array mese area and bedrooms ko divide krke hata deta hai
    text= ",".join(text)
    return text


data["clean_info"]=data["info"].apply(clean_function)

data[["area","bedrooms"]]=data["clean_info"].str.split(",", expand=True)#this is the important liner for this code
features=data[["area","bedrooms"]]
target =data["price"]

model = LinearRegression()
model.fit(features.values,target)
print(features)

area=float(input("enter the area"))
bedrooms=float(input("enter the no. of bedrooms"))

result=model.predict([[area,bedrooms]])
print(result)