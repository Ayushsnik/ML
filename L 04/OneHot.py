import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv("Code2_OneHot.csv")

features= data[["state","city", "area"]]
new_features = pd.get_dummies(features)
target = data["price"]

#print(features)
#print(new_features)

model = LinearRegression()
model.fit(new_features.values, target)

area = float(input("please enter area: "))
state = int(input("1.guj  2.mah"))
price= 0


if state==1:
    city = int(input("1.amd  2.surat"))
    if city==1:
        price = model.predict([[area, 1, 0, 1, 0, 0, 0]])
    elif city==2:
        price = model.predict([[area, 1, 0, 0, 0, 0, 1]])
    else:
        print("invalid input")
elif state==2:
    city = int(input("1.mumbai  2.pune"))
    if city==1:
        price = model.predict([[area, 0, 1, 0, 1, 0, 0]])
    elif city==2:
        price = model.predict([[area, 0, 1, 0, 0, 1, 0]])
    else:
        print("invalid input")
else:
    print("invalid input")

print("the price is: ", price)

