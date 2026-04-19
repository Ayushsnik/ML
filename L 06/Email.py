import pandas as pd
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("Code1_NB.csv")
features = data.drop(["Index",'Result'], axis=1)
target = data['Result']

new_features = pd.get_dummies(features)
print(new_features)

model = BernoulliNB()
model.fit(new_features.values, target)


dear = int(input("1.Dear yes 2.No "))
if dear == 1:
    a1 =[0,1]
else:
    a1 = [1,0]

friend = int(input("1.Friend yes 2.no "))
if friend == 1:
    a2 =[0,1]
else:
    a2 = [1,0]

lunch = int(input("1.Lunch yes 2.no "))
if lunch == 1:
    a3 =[0,1]
else:
    a3 = [1,0]

money=int(input("1.Money yes 2.no "))
if money == 1:
    a4 =[0,1]
else:
    a4 = [1,0]


a5 =[a1+a2+a3+a4]
result= model.predict(a5)
print(result)

