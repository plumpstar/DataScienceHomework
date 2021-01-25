import requests
from pyquery import PyQuery as pq

comments_url = 'https://m.weibo.cn/comments/hotflow?id='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.198 Safari/537.36'
}
# 输出文件
file = 'D:\数据\文本\第四阶段\\5月28日.txt'
fp = open(file, 'a+', encoding='utf-8')

cnt = open('D:\数据\筛选\第四阶段\\5月28日.csv', 'r')
i = 1
for line in cnt:
    print(i)
    id = line.strip().split(',')[0]
    com_true_url = comments_url + id + '&mid=' + id
    print(com_true_url)
    rs = requests.get(com_true_url, headers=headers)
    obj = rs.json()
    if obj.get('ok') == 1:
        comment_arr = obj.get('data').get('data')
        for d in comment_arr:
            fp.write(pq(d.get('text')).text())
            fp.write('\n')
    fp.write('\n')
    i += 1
fp.close()
