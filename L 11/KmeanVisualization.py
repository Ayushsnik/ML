import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("Code1_KNN.csv")
features = data[["X","Y"]]

model = KMeans(n_clusters=2, random_state= 0 )  #random state lock karnekeliye ha 0 and 1 shuffle nai karga
cluster = model.fit_predict(features.values)


data["Group"] = cluster
print(data)

cluster1 = data[data.Group == 1]
cluster2 = data[data.Group == 0]

centroid1 = model.cluster_centers_[1]
centroid2 = model.cluster_centers_[0]



print(centroid1)
print(centroid2)
plt.figure(figsize=(11,6))
plt.scatter(cluster1["X"], cluster1["Y"], color="red", label="Cluster1")
plt.scatter(cluster2["X"], cluster2["Y"], color="blue", label="Cluster2")
plt.scatter(centroid1[0], centroid1[1], color="pink", marker="x")
plt.scatter(centroid2[0], centroid2[1], color="purple", marker="x")  #marker is
plt.legend()
plt.show()

