import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.classifier import LogisticRegression
from mlxtend.regressor import LinearRegression
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("Code4_LoR.csv")
data = data.sort_values(by="hours")
features = data[["hours"]]
target = data["result"]

model = LogisticRegression()
model.fit(features.values, target)

plt.figure(figsize = (10,5))
plt.scatter(data["hours"],data["result"])
plt.plot(data["hours"],model.predict(features.values))
plt.title("exam")
plt.xlabel("hours")
plt.ylabel("result")
plt.show()