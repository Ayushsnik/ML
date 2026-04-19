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

m = model.coef_
c = model.intercept_

print("m is:",m)
print("c is: ",c)

years = int(input("enter years: "))
salary= m*years + c

print("salary is: ", salary, "lakhs")

