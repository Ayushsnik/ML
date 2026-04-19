import pandas as pd
from pyexpat import features
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Code3.csv")

features = data[["area", "bedrooms"]]
target = data["price"]

model = LinearRegression()
model.fit(features.values, target)

area = float(input("enter area:"))
bedrooms = int(input("enter bedrooms:"))

price = model.predict([[area, bedrooms]])
print("The price is: ", price )