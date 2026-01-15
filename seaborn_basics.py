import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
data = sns.load_dataset("tips")

# Histogram
sns.histplot(data["total_bill"])
plt.title("Total Bill Distribution")
plt.show()

# Box Plot
sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Bill Amount by Day")
plt.show()
