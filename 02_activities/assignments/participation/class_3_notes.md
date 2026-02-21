# Class 3 Notes – Customizing + Subplots

## Legends
- add label inside plot()
- then call ax.legend()
- can change:
  - location
  - fontsize
  - frame
  - number of columns
- can move legend outside plot using bbox_to_anchor

---

## Text + Annotations
- use ax.text(x, y, "text")
- can change:
  - color
  - size
  - alignment (ha)
- annotate() adds arrows
  - need xy (where arrow points)
  - xytext (where text goes)
  - arrowprops for style

---

## Axis stuff
- can remove ticks with:
  - NullLocator
  - NullFormatter
- can limit ticks with MaxNLocator
- can set intervals with MultipleLocator
- rotate labels using plt.xticks(rotation=45)

---

## Subplots
- fig, (ax1, ax2) = plt.subplots(ncols=2)
- figure holds axes
- each axes is its own plot
- can customize each separately

---

## Layout
- sometimes labels get cut off
- tight layout
- constrained layout (better)

---

## Multiple plots on same axes
- just call multiple plot methods on same ax
- can combine bar + line

---

## Error bars
- calculate std with np.std()
- use ax.errorbar()
- yerr = value
- can customize color, width, caps
- errorevery controls frequency

---

## Images in plots
- use PIL + requests
- add new axes with fig.add_axes()
- use imshow()
- turn axis off