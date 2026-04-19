import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("flat_price.csv")
features = data[["place", "area"]]
target = data["price"]

new_features = pd.get_dummies(features)

model = LinearRegression()
model.fit(new_features.values, target)

area = float(input("please enter area: "))
choice = int(input("1.Karjat 2.khandala 3.Lonavla"))

if choice == 1:
    price= model.predict([[area, 1,0,0]])
elif choice == 2:
    price = model.predict([[area, 0,1,0]])
elif choice == 3:
    price = model.predict([[area, 0,0,1]])
else:
    print("invalid input")
    exit(0)

print("The price is: ", price)