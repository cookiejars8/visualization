# Class 1 Participation - Data Visualization Intro

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests


# ---------------------------
# Create sample data
# ---------------------------
np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0, 100, 50)


# ---------------------------
# Scatterplot
# ---------------------------
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)
ax.set_title("Basic Scatterplot")
plt.show()


# ---------------------------
# Bar plot
# ---------------------------
fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(x, y)
ax.set_title("Bar Plot Example")
plt.show()


# ---------------------------
# Line plot
# ---------------------------
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title("Line Plot Example")
plt.show()


# ---------------------------
# Histogram
# ---------------------------
fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(y)
ax.set_title("Histogram Example")
plt.show()


# ---------------------------
# Customizing labels and fonts
# ---------------------------
font1 = {'family': 'sans-serif', 'color': 'blue', 'size': 18}
font2 = {'family': 'monospace', 'color': 'green', 'size': 12}

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)

ax.set_title("Customized Plot", fontdict=font1)
ax.set_ylabel("Y Values", fontdict=font2)
ax.set_xlabel("X Values", fontdict=font2)

fig.tight_layout()
plt.show()


# ---------------------------
# Customizing markers and line style
# ---------------------------
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(
    x,
    y,
    marker='*',
    markersize=10,
    color='#7425b9',
    linestyle='--',
    linewidth=2,
    markeredgecolor='#fa9359',
    markerfacecolor='#000000'
)

ax.grid(axis='y')
ax.set_title("Fully Customized Plot")
plt.show()