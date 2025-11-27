import matplotlib.patches as p
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
steps = [
    ("Token Embedding", 0.8),
    ("Positional Encoding", 0.6),
    ("Multi-Head Attention", 0.4),
    ("Feed-Forward", 0.2),
    ("Output", 0.0)
]
for label, y in steps:
    ax.add_patch(p.Rectangle((0.25, y), 0.5, 0.10))
    ax.text(0.5, y+0.05, label, ha='center', va='center')
for i in range(len(steps)-1):
    _, y1 = steps[i]
    _, y2 = steps[i+1]
    ax.annotate("", xy=(0.5, y2+0.10), xytext=(0.5, y1),arrowprops=dict(arrowstyle="->"))
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis('off')
plt.show()
