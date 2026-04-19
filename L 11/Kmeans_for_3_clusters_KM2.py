import pandas as pd
from sklearn.cluster import KMeans
data = pd.read_csv("Code2_KNN.csv")

features = data[["A","B"]]

model = KMeans(n_clusters=2, random_state= 0, init= "k-means++" )
cluster = model.fit_predict(features.values)


data["Group"] = cluster
print(data)

x= float(input("enter A: "))
y= float(input("enter B11: "))

result = model.predict([[x,y]])
print(result)

