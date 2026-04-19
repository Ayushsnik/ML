import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Code1.csv")
features = data[["area"]]
target = data["price"]
model = LinearRegression()
model.fit(features.values, target)

area = float(input("please enter area: "))
price = model.predict([[area]])

print("the price is", price)
