import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = pd.read_csv("Code_6.csv")
text = " ".join(data["fruit"])
print(text)

wc = WordCloud(
    max_words=50,
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