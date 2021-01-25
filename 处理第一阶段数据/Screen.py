
cnt = open('D:\数据\\firstStageId.csv', 'r')
file = './newFirstStageId.csv'
fp = open(file, 'w', encoding='utf-8')
fp.write('id,comments\n')
for line in cnt:
    if line.strip().split(',')[0] == 'id':
        continue
    if int(line.strip().split(',')[1]) > 600:
        continue
    fp.write(line)
    # fp.write(line.strip().split(',')[0] + '\n')

cnt.close()
fp.close()
