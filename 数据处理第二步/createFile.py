



for j in range(1, 13):
    for k in range(1, 32):
        filename = 'D:\微博数据\分类\\' + str(j) + '月' + str(k) + '日.csv'
        f = open(file=filename, mode='w', encoding='utf-8')
        f.close()
