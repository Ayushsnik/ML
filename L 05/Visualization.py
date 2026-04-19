import pandas as pd
import matplotlib.pyplot as plt

data =  pd.read_csv("Code4_LoR.csv")

plt.figure(figsize = (10,5))
plt.scatter(data["hours"],data["result"])
plt.title("exam")
plt.xlabel("hours")
plt.ylabel("result")
plt.show()

