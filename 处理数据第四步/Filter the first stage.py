cnt = open('D:\数据\汇总\\第一阶段.csv', 'r')
file = './newFirstStageId.csv'
fp = open(file, 'w', encoding='utf-8')
for line in cnt:
    if line.strip().split(',')[0] == 'id':
        continue
    if int(line.strip().split(',')[1]) == 0:
        continue
    if int(line.strip().split(',')[1]) == 1:
        continue
    if int(line.strip().split(',')[1]) == 2:
        continue
    if int(line.strip().split(',')[1]) == 3:
        continue
    if int(line.strip().split(',')[1]) == 4:
        continue
    if int(line.strip().split(',')[1]) > 300:
        continue
    fp.write(line)
    # fp.write(line.strip().split(',')[0] + '\n')

cnt.close()
fp.close()
