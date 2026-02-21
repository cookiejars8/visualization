import numpy as np
import matplotlib.pyplot as plt

# Class 4 Participation
# Topic: accessible data visualization + advocacy

np.random.seed(613)

# Fake data (just for class practice)
x = np.arange(1, 11)
group_a = np.random.randint(10, 40, 10)
group_b = np.random.randint(10, 40, 10)

# -------------------------
# 1) Accessible-ish line chart
# - don't rely only on colour (use markers + line styles)
# - readable labels + bigger font
# -------------------------
plt.rcParams.update({"font.size": 12})  # keep text readable (basic attempt)

fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(x, group_a, marker="o", linestyle="-", label="Group A")
ax.plot(x, group_b, marker="s", linestyle="--", label="Group B")

ax.set_title("Example: Two Groups Over Time (Readable + Labeled)")
ax.set_xlabel("Week")
ax.set_ylabel("Value")
ax.legend()
ax.grid(True, axis="y", alpha=0.3)

# simple “alt-text” idea (for screen readers / descriptions)
alt_text = (
    "Line chart showing Group A and Group B over 10 weeks. "
    "Group A is a solid line with circle markers, Group B is a dashed line with square markers. "
    "Values range roughly from 10 to 40."
)
# (In real use, alt-text would be placed where the chart is published.)

plt.tight_layout()
plt.show()


# -------------------------
# 2) Colormap example (viridis)
# viridis is often more colourblind/grayscale friendly than rainbow maps
# -------------------------
data = np.random.normal(size=(30, 30))

fig, ax = plt.subplots(figsize=(5, 4))
img = ax.imshow(data, cmap="viridis")  # accessible-ish colormap
ax.set_title("Heatmap Using Viridis Colormap")
fig.colorbar(img, ax=ax)
plt.tight_layout()
plt.show()


# -------------------------
# 3) Tiny “advocacy” example
# Same data, but framing changes interpretation (title + annotation)
# -------------------------
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(x, group_a, color="#3b4cc0")  # using a single strong colour to keep it simple
ax.set_title("Where Are We Falling Behind? (Framing Example)")
ax.set_xlabel("Week")
ax.set_ylabel("Value")

# annotation = draws attention (persuasive tool)
worst_week = int(x[np.argmin(group_a)])
worst_value = int(np.min(group_a))

ax.annotate(
    "Lowest point",
    xy=(worst_week, worst_value),
    xytext=(worst_week + 1, worst_value + 10),
    arrowprops=dict(arrowstyle="->", color="black")
)

ax.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# NOTE: This is just an example of how visuals can be persuasive.
# Real advocacy charts should include sources + context.