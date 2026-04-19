import pandas as pd
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("Code0_NB.csv")
features = data[["Weather", "Car"]]
target = data["Result"]

new_features = pd.get_dummies(features)
# print(new_features)

model = BernoulliNB()
model.fit(new_features.values, target)

weather = int(input("1. Sunny 2. Rainy"))
if weather == 1:
    a1 = [0, 1]
else:
    a1 = [1, 0]

car = int(input("1. Working 2. Broken"))
if car == 1:
    a2 = [0, 1]
else:
    a2 = [1, 0]

# a1 and a2 khud array hai and a3 another array isiliye [[]] double bracket
a3 = [a1 + a2]
result = model.predict(a3)
print(result)