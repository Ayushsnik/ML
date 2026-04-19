import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("Code1_KNN.csv")

features = data[["Height(cm)", "Weight(kg)"]]
target = data["T-Shirt Size"]


k= int(len(data) ** 0.5)
if k % 2 ==0:
    k=k+1

mms = MinMaxScaler()
scaled_features = mms.fit_transform(features.values)

model = KNeighborsClassifier(n_neighbors=k)
model.fit(scaled_features, target)

height = int(input("enter height: "))
weight = int(input("enter weight: "))

a1= [[height,weight]]
scaled_a1 = mms.transform(a1)

result = model.predict(scaled_a1)
print (result)

