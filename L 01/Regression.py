import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data = pd.read_csv("Code1.csv")
features = data[["area"]]
target = data["price"]

model = LinearRegression()
model.fit(features, target)
plt.figure(figsize=(10,5))
plt.scatter(data["area"], data["price"])
plt.plot(data["area"], model.predict(features))
plt.title("Powai Estate Rate")
plt.xlabel("area")
plt.ylabel("price")
plt.show()