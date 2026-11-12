import matplotlib.pyplot as plt
from data.generator import make_dataset

df = make_dataset(seed=0)

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(df.index, df["value"], lw=0.6)
bad = df[df["label"] == 1]
ax.scatter(bad.index, bad["value"], s=4, c="red")
ax.set_title("Synthetic traffic with injected anomalies")
plt.savefig("plots/synthetic_example.png", dpi=150)
print("saved")