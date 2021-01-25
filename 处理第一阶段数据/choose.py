import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

cnt = pd.read_csv('D:\DataScienceHomework\处理第一阶段数据\\newFirstStageId.csv')
x = cnt['comments']
mu = np.mean(x)
sigma = np.std(x)
print(mu)
print(sigma)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
num_bins = 150
n, bins, patches = plt.hist(x, num_bins, density=True, facecolor='blue', alpha=0.5)
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('comments')
plt.ylabel('numbers')
plt.title(u'评论数分布:$\mu=156.27$,$\sigma=134.81$')
plt.subplots_adjust(left=0.15)
plt.show()
