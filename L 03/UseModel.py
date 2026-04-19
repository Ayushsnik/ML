from pickle import *

f = open("ayush.pkl", "rb")
model = load(f)
f.close()

temp1 = float(input("Enter area: "))
temp2 = float(input("Enter bedrooms: "))
price = model.predict([[temp1, temp2]])
print("The price is: ", price)
