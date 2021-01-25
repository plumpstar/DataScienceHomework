# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


f = pd.read_csv('E:\Python\HanLP分词\心态分析\第一阶段心态值.csv')
x = f['index']
y = f['value']

plt.title('Analysis of Mentality In The First Stage')

plt.plot(x, y, color='skyblue')


plt.legend() # 显示图例

plt.xlabel('times')

plt.ylabel('value')

plt.show()
