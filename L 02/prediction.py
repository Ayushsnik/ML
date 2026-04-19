import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Code2 - Copy.csv")
print(data.isnull().sum)
data = data.dropna()
# print(data.isnull.sum())

features = data[["years"]]
target = data["salary"]
model = LinearRegression()
model.fit(features.values,target)

years = int(input("please enter years: "))
salary = model.predict([[years]])


print("salary is: ", salary, "lakhs")

