import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("Code2_KNN2.csv")

features = data[["Weight", "Height"]]
target = data["Class"]


k= int(len(data) ** 0.5)
if k % 2 ==0:
    k=k+1

mms = MinMaxScaler()
scaled_features = mms.fit_transform(features.values)

model = KNeighborsClassifier(n_neighbors=k)
model.fit(scaled_features, target)

weight = int(input("enter weight: "))
height = int(input("enter height: "))

a1= [[height,weight]]
scaled_a1 = mms.transform(a1)

result = model.predict(scaled_a1)
print (result)

