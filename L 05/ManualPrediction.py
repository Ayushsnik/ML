import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("Code4_LoR.csv")
feature = data[["hours"]]
target = data["result"]

model = LogisticRegression()
model.fit(feature.values,target)

m= model.coef_
c= model.intercept_

temp = float(input("enter hours: "))
result = 1/(1+(2.71 ** -(c+m*temp)))


if result<.5:
    print("fail")
else:
    print("pass")