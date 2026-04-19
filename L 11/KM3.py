import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

data = pd.read_csv("Code3_KNN.csv")
features = data[["RUNS","WICKETS"]]

mms = MinMaxScaler()
scaled_features = mms.fit_transform(features.values)

model = KMeans(n_clusters=2, random_state= 0, init= "k-means++" )
cluster = model.fit_predict(scaled_features)

data["Groups"] = cluster
print(data)

runs = int(input("Enter the number of runs: "))
wickets = int(input("Enter the number of wickets: "))

a1 = [[runs, wickets]]
scaled_features = mms.transform(a1)

result = model.predict(scaled_features)


if(result ==1):
    print("batsman")
else:
    print("bowler")
