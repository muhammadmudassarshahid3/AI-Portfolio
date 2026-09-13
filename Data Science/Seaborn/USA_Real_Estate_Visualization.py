import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df = pd.read_csv(r'c:\Users\user\Documents\GitHub\Full-Stack-AI-Bootcamp-B-11\Week4\RealEstate-USA (2).csv')
print(df.head())
print(df.columns)
print(df.dtypes)
sns.set(style="whitegrid")
g=sns.displot(data=df, x="bed", y="price", kind="hist")
g.figure.suptitle("bedrooms vs price", y=1.02)
g.figure.show()
g=sns.displot(data=df, x="bed",y="price", kind="kde")
g.figure.suptitle("bedroom vs price - kde", y=1.02)
g.figure.show()
sns.scatterplot(data=df, x="house_size", y="price")
plt.title("house_size vs price")
plt.show()
sns.lineplot(data=df, x="house_size", y="price")
plt.title("house_size vs price")
plt.show()
sns.barplot(data=df, x="house_size", y="price")
plt.title("house_size vs price")
plt.show()