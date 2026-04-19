import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data= pd.read_csv("Code2_DT.csv")
features = data.drop(["Day","PlayTennis"],axis=1)
target= data["PlayTennis"]
new_features = pd.get_dummies(features)

model = DecisionTreeClassifier()
model.fit(new_features.values,target)

df=pd.DataFrame(new_features)
df.to_csv("BOOK1.csv")

result= model.predict([[0,0,1,0,1,0,1,0,0,1]])
print(result)