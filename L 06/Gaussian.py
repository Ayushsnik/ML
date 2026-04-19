import pandas as pd
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv("Code2_GB.csv")
features = data.drop(["User ID", "Purchased"],axis=1)
target = data["Purchased"]
new_features = pd.get_dummies(features)

model = GaussianNB()
model.fit(new_features.values, target)

# print(new_features)

age = int(input("Enter age "))
salary = int(input("Enter salary "))

gender = int(input("1.male 2.female"))
if gender ==1:
    result= model.predict([[age, salary,1,0]])
else:
    result= model.predict([[age, salary, 0,1]])
print(result)