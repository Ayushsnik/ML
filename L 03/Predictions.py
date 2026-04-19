import pandas as pd
from pyexpat import features
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("Code3.csv")
features = data[["area", "bedrooms"]]
target = data["price"]

x_train, x_test, y_train, y_test = train_test_split(features.values, target)
model = LinearRegression()
model.fit(features.values, target)

training_score = model.score(x_train, y_train)
testing_score = model.score(x_test, y_test)

print("Training score: ", training_score*100)
print("Testing score: ", testing_score*100)

temp1 = float(input("Enter area: "))
temp2 = float(input("Enter bedrooms: "))
price = model.predict([[temp1, temp2]])
print("The price is: ", price)