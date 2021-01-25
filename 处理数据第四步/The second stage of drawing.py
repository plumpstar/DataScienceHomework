import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

cnt = pd.read_csv('D:\DataScienceHomework\处理数据第四步\\newSecondStageId.csv')
x = cnt['comments']
mu = np.mean(x)
sigma = np.std(x)
print(mu)
print(sigma)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
num_bins = 200
n, bins, patches = plt.hist(x, num_bins, density=True, facecolor='green', alpha=0.5)
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('评论数')
plt.ylabel('比率')
plt.title(u'第二阶段评论数分布:$\mu=92.80$,$\sigma=78.60$')
plt.subplots_adjust(left=0.15)
plt.show()
