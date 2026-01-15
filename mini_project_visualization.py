import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [10000, 12000, 15000, 18000]
}

df = pd.DataFrame(data)

plt.bar(df["Month"], df["Revenue"])
plt.title("Monthly Revenue Analysis")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
