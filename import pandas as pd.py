import pandas as pd
import matplotlib.pyplot as plt

# 构造示例数据（非真实值）
data = {
    "Year": [y for y in range(2013, 2023)],
    "US_LPR": [3.25, 3.25, 3.50, 3.75, 3.75, 4.00, 4.25, 4.50, 4.75, 5.25],
    "Japan_LPR": [1.45, 1.40, 1.38, 1.35, 1.30, 1.25, 1.20, 1.15, 1.10, 1.05]
}

df = pd.DataFrame(data)

plt.plot(df["Year"], df["US_LPR"], label="US LPR")
plt.plot(df["Year"], df["Japan_LPR"], label="Japan LPR")
plt.xlabel("Year")
plt.ylabel("LPR (%)")
plt.title("近十年美日LPR示例")
plt.legend()
plt.show()