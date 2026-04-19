import pandas as pd
from scipy.cluster.hierarchy import centroid
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("Code2_KNN.csv")

features = data[["A","B"]]

model = KMeans(n_clusters=3, random_state= 0, init= "k-means++" )
cluster = model.fit_predict(features.values)


data["Group"] = cluster
print(data)

cluster1 = data[data["Group"] == 0]
cluster2 = data[data["Group"] == 1]
cluster3 = data[data["Group"] == 2]

centroid1 = model.cluster_centers_[0]
centroid2 = model.cluster_centers_[1]
centroid3 = model.cluster_centers_[2]

plt.figure(figsize=(11,6))
plt.scatter(cluster1["A"],cluster["B"], color = "red", label = "Red->Cluster 1")
plt.scatter(cluster1["A"],cluster["B"], color = "green", label = "Green->Cluster 2")
plt.scatter(cluster1["A"],cluster["B"], color = "Blue", label = "Blue->Cluster 3")


plt.scatter(centroid1[0], centroid1[1], marker ="x")
plt.scatter(centroid2[0], centroid2[1], marker ="x")
plt.scatter(centroid3[0], centroid3[1], marker ="x")


plt.legend()
plt.show()

