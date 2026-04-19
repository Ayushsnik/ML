import pandas as pd 
from sklearn.linear_model import LinearRegression
from pickle import dump

data = pd.read_csv("phone_data.csv")

features = data[[
    "Daily_Usage_Hours",
    "Sleep_Hours",
    "Academic_Performance",
    "Phone_Checks_Per_Day",
    "Weekend_Usage_Hours"
]]

target = data["Addiction_Level"]

model = LinearRegression()
model.fit(features.values, target)

f = open("addict.pkl", "wb")
dump(model, f)
f.close()