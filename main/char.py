# %%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from random import *
# %%

stock_list = []

for _ in range(12):
    i = randint(1000, 150000)
    stock_list.append(i)
    print(i)    
# %%
x = np.arange(12)
y = np.array(stock_list)

# %%
max_price = max(stock_list)
min_price = min(stock_list)
mean_price = np.mean(stock_list)
end_price = stock_list[-1]
# %%
print(f"최고가: {max_price}")
print(f"최저가: {min_price}")
print(f"종시가: {end_price}")
print(f"평군가 추이: {mean_price}")
# %%
fig, ax = plt.subplots(1, 1, figsize=(10, 10), facecolor='white')
ax.plot(stock_list, color='mediumslateblue')
ax.scatter(x=x, y=stock_list)
ax.set_facecolor("white")

for i, text in enumerate(stock_list):
    ax.annotate(str(text), (x[i], y[i]+2500), fontsize=13, color='mediumspringgreen')
plt.title(f"ROS Stock Chart: \nmax = {max_price}, min = {min_price}, mean = {mean_price:.2f}, end = {end_price}", fontsize=20)
plt.xlabel("Time", fontsize=15)
plt.ylabel("Price", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid()
plt.show()
# %%
