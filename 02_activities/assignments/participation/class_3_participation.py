import numpy as np
import matplotlib.pyplot as plt

# set seed so it's reproducible
np.random.seed(613)

# sample data
x = np.arange(50)
y1 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

# -----------------------------
# 1. Line plot with legend
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 3))

ax.plot(x, y1, label="Person 1")
ax.plot(x, y2, label="Person 2")

ax.legend(loc="lower right")

plt.title("Line Plot with Legend")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()


# -----------------------------
# 2. Scatter with annotation
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 3))

ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")

ax.legend()

ax.annotate(
    "Important point!",
    xy=(10, y1[10]),
    xytext=(20, 90),
    arrowprops=dict(arrowstyle="->", color="red")
)

plt.title("Scatter with Annotation")
plt.show()


# -----------------------------
# 3. Subplots example
# -----------------------------
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 3))

ax1.scatter(x, y1)
ax1.set_title("Scatter Plot")

ax2.plot(x, y2)
ax2.set_title("Line Plot")

plt.show()


# -----------------------------
# 4. Error bars
# -----------------------------
y2_sd = np.std(y2)

fig, ax = plt.subplots(figsize=(6, 3))

ax.plot(x, y2, color="red")

ax.errorbar(
    x,
    y2,
    yerr=y2_sd,
    fmt="none",
    ecolor="black",
    capsize=4,
    errorevery=5
)

plt.title("Line Plot with Error Bars")
plt.show()


# -----------------------------
# 5. Multiple viz on same axes
# -----------------------------
categories = ["A", "B", "C", "D", "E"]
values1 = np.array([10, 20, 30, 15, 25])
values2 = np.array([12, 18, 28, 20, 10])

fig, ax = plt.subplots(figsize=(6, 3))

ax.bar(categories, values1, color="indigo")
ax.plot(categories, values2, color="red")

plt.title("Bar + Line Together")
plt.show()