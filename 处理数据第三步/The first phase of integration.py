i = 1
fp = open('D:\数据\汇总\第一阶段.csv', mode='a+', encoding='utf-8')
while i <= 46:
    print(i)
    filename = 'D:\汇总\第一阶段\第一阶段' + ' (' + str(i) + ').csv'
    f = open(file=filename, mode='r', encoding='utf-8')
    for line in f:
        fp.write(line)
    f.close()
    i += 1
fp.close()
