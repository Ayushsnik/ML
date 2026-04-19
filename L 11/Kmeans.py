import pandas as pd
from sklearn.cluster import KMeans
data = pd.read_csv("Code1_KNN.csv")

features = data[["X","Y"]]

model = KMeans(n_clusters=2, random_state= 0, init= "k-means++" )
cluster = model.fit_predict(features.values)


data["Group"] = cluster
print(data)

x= float(input("enter x: "))
y= float(input("enter y: "))

result = model.predict([[x,y]])
print(result)

