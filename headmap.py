import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv("sudan_trade_data.csv")

# Create a Pivot Table: Rows = Neighbors, Columns = Items, Values = Total USD
pivot = df.pivot_table(index='Neighbor', columns='Item', values='Value_USD', aggfunc='sum')

# Plotting the Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlOrRd")
plt.title("Conflict Trade Intensity Heatmap")
plt.show()