
cnt = open('D:\数据\\firstStageId.csv', 'r')
file = './Id.csv'
fp = open(file, 'w', encoding='utf-8')
for line in cnt:
    if line.strip().split(',')[0] == 'id':
        continue
    if int(line.strip().split(',')[1]) <= 156:
        continue

    fp.write(line.strip().split(',')[0] + '\n')

cnt.close()
fp.close()