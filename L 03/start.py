import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("startup_data.csv")
features = data[["RD_Spend","Administration","Marketing Spend"]]
target = data["Profit"]
x_train, x_test, y_train, y_test = train_test_split(features.values,target)

model= LinearRegression()
model.fit(x_train, y_train)
training_score = model.score(x_train,y_train)

testing_score = model.score(x_test, y_test)


print("Training score : ",training_score*100)
print("Testing score : ",testing_score*100)

temp1 = float(input("Enter RD_Spend: "))
temp2 = float(input("Enter Administration: "))
temp3 = float(input("Enter marketing Spend: "))

price = model.predict([[temp1, temp2, temp3]])

print("The profit is ",price)