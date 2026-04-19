import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("Code2_RF.csv")
data.columns = ["buying","maintenance","doors","person","lg_boot","safety","class"]

features = data.drop(["class"], axis=1)
target = data["class"]

new_features = pd.get_dummies(features)

x_train, x_test, y_train, y_test = train_test_split(new_features.values, target)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(x_train, y_train)

cr = classification_report(y_test, model.predict(x_test))
print(cr)

df = pd.DataFrame(new_features)
df.to_csv("Book1.csv")

result = model.predict([[0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1]])
print(result)