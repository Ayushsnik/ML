import pandas as pd
data = pd.read_csv("Code1_Data_Preprocessing.csv")
print(data.isnull().sum())
print(data)

#type 1 : to drop the null values
#data = data.dropna()
#print(data.isnull().sum())


#type 2 : to fill null values with constant values
data = data.fillna({"price": 8})
print(data)

#type 3: to fill null values with the mean values
mean = data["price"].mean()
data = data.fillna({"price":mean})

#type 4: to fill null values with the median values
median = data["price"].median()
data = data.fillna({"price":median})

