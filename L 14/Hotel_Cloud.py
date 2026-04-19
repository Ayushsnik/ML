import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt


data = pd.read_csv('Book2.csv')
positive_data = data[data.label=="positive"]
print("positive_data")

text = " ".join(positive_data["Review"])
print(text)

wc = WordCloud(
    width = 608,
    height = 400,
    colormap = "viridis",
    background_color = "white",
).generate(text)


plt.figure(figsize=(10,5))
plt.imshow(wc)
plt.axis("off")
plt.savefig("fruits.pdf")
plt.show()

