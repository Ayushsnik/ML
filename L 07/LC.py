import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("Code3_LC.csv")

features = data.drop(["LUNG_CANCER"],axis=1)
new_features = pd.get_dummies(features)

mms = MinMaxScaler()
scaled_features = mms.fit_transform(new_features.values)
target = data["LUNG_CANCER"]

k =int(len(data)**.5)
if k%2==0:
    k=k+1

model =KNeighborsClassifier(n_neighbors=k)
model.fit(scaled_features,target)

# a1 = [[59,1,1,1,2,1,2,1,2,1,2,2,1,2,1,0]]
# scaled_a1 = mms.transform(a1)
# result = model.predict(scaled_a1)

df = pd.DataFrame(scaled_features)
df.to_csv("BOOK.csv")

scaled_features= [[0.727272727,0,1,1,0,0,1,0,1,1,1,1,1,1,0,1]]
result = model.predict(scaled_features)
print(result)