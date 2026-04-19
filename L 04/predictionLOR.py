import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("Code4_LoR.csv")

features = data[["hours"]]
target = data["result"]

model = LogisticRegression()
model.fit(features.values, target)

temp1 = float(input("please enter hours: "))
result = model.predict([[temp1]])
if result == 1:
    print("pass")
else:
    print("chud gaye guru")
# print("congratulations your result is: ", result)