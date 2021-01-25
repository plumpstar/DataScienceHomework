import json

file = 'D:\数据\中国之声Id.csv'  # 输出文件名
fpf = open(file, 'a+', encoding='utf-8')

i = 1328  # 起始页
while i <= 1355:  # 终止页
    print(i)
    file2 = 'D:\微博数据\中国之声\中国之声getIndex' + str(i) + '.json'

    fp = open(file2)
    dic = json.load(fp)  # 将json格式文件加载成为字典

    items = dic.get('data').get('cards')  # 每一页博文的数组

    for item in items:  # 遍历数组
        itemSuc = item.get('mblog')

        if itemSuc is None:  # 可能有空的情况
            continue

        k = str(itemSuc.get('id'))
        fpf.write(k)
        fpf.write(',')
        v = str(itemSuc.get('comments_count'))
        fpf.write(v)
        fpf.write(',')
        fpf.write(itemSuc.get('created_at'))
        fpf.write('\n')
    i += 1
    fp.close()
fpf.close()
