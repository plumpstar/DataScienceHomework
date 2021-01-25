three = {
    '第三阶段 (1)': '2月10日',
    '第三阶段 (2)': '2月11日',
    '第三阶段 (3)': '2月12日',
    '第三阶段 (4)': '2月13日',
}

i = 1
while i <= 4:
    print(i)
    filename = 'D:\汇总\第三阶段\第三阶段' + ' (' + str(i) + ').csv'
    f = open(file=filename, mode='r', encoding='utf-8')
    output = 'D:\数据\筛选\第三阶段\\' + three.get('第三阶段' + ' (' + str(i) + ')') + '.csv'
    fp = open(file=output, mode='a+', encoding='utf-8')
    for line in f:
        if int(line.strip().split(',')[1]) > 84:
            fp.write(line)
    fp.close()
    f.close()
    i += 1
