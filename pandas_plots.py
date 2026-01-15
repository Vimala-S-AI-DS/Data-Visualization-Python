import pandas as pd

data = {
    "Year": [2019, 2020, 2021, 2022],
    "Sales": [200, 250, 300, 350]
}

df = pd.DataFrame(data)

df.plot(x="Year", y="Sales", kind="line", title="Yearly Sales")
