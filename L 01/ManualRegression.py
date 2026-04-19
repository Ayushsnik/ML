import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Code1.csv")
features = data[["area"]]
target = data["price"]
model = LinearRegression()
model.fit(features.values, target)

area = float(input("please enter area: "))
m= model.coef_
c= model.intercept_

print("the price is", m)
print("the price is", c)
price = m* area + c

print("the price is", price)
