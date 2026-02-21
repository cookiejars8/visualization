# Class 5 Participation - Beyond Matplotlib
# Seaborn, Plotly, Wordclouds, Venn diagrams

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Seaborn basics (tips dataset)
# -----------------------------
sns.set_style("whitegrid")  # preset style

tips = sns.load_dataset("tips")
print(tips.head())

# line plot (tip vs total bill)
tipgraph = sns.lineplot(data=tips, x="total_bill", y="tip")
tipgraph.set(title="Tips vs Total Bill", xlabel="Total Bill ($)", ylabel="Tip Amount ($)")
plt.show()

# scatter plot with extra variables (hue + style)
tipgraph2 = sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    style="time",
    hue="day"
)
tipgraph2.set(title="Tips vs Total Bill (Hue + Style)", xlabel="Total Bill ($)", ylabel="Tip Amount ($)")
plt.show()

# pairplot (this makes multiple plots at once)
sns.pairplot(data=tips, hue="day")
plt.show()


# -----------------------------
# Plotly basic interactive plot
# -----------------------------
import plotly.graph_objects as go

x1 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110, 180, 240, 99, 220])

graph = go.Figure()
graph.add_trace(go.Bar(x=x1, y=y1))
graph.update_layout(title="Pirate Scores", xaxis_title="Pirates", yaxis_title="Score")
graph.show()


# -----------------------------
# Wordcloud example
# -----------------------------
from wordcloud import WordCloud

df = pd.read_csv(
    "https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/movie_quotes.csv",
    on_bad_lines="skip"
)

text = " ".join(each for each in df.quote.astype(str))

wordcloud = WordCloud(background_color="white", colormap="inferno").generate(text)

fig, ax = plt.subplots(figsize=(7, 3))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
plt.show()


# -----------------------------
# Venn diagram example
# -----------------------------
from matplotlib_venn import venn2_unweighted

A = set(["apple", "banana", "watermelon"])
B = set(["pumpkin", "blueberry", "apple", "key lime"])

diagram = venn2_unweighted(
    [A, B],
    set_labels=("Fruits", "Pies"),
    set_colors=("blue", "red"),
    alpha=0.5
)
plt.show()

# optional: show words instead of counts
diagram.get_label_by_id("10").set_text("\n".join(A - B))
diagram.get_label_by_id("11").set_text("\n".join(A & B))
diagram.get_label_by_id("01").set_text("\n".join(B - A))
plt.show()