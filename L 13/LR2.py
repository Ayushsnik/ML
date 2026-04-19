import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Code2.csv")

def clean_function(text):
    text = text.replace(";","")
    return text

data["clean_info"] = data["info"].apply(clean_function)

data[["area","bedrooms"]]= data["clean_info"].str.split(",",expand= True)
features = data[["area","bedrooms"]]
target = data["price"]

model = LinearRegression()
model.fit(features.values,target)
print(features)

area = float(input("Enter the area: "))
bedrooms = int(input("Enter the bedrooms: "))

result = model.predict([[area,bedrooms]])
print(result)