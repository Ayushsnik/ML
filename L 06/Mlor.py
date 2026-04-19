import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("Code1_MLoR.csv")
features = data[["Age"]]
target = data["Vehicle"]

x_train, x_test, y_train, y_test = train_test_split(features.values, target)

model = LogisticRegression()
model.fit(x_train, y_train)

cr= classification_report(y_test, model.predict(x_test))
print(cr)

#
# temp1= int(input("Enter the age: "))
# result=model.predict([[temp1]])
# print(result)
# print(model.predict_proba([[temp1]]).round(2)*100)