import matplotlib.pyplot as plt
from data.generator import make_series

df = make_series(seed=0)
df["value"].plot(figsize=(14, 4), lw=0.6)
plt.title("Normal traffic, 14 days")
plt.savefig("plots/normal_data.png", dpi=150)
print("saved")