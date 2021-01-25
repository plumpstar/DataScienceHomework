import os
import requests
import time
i = 2189  # 起始页数

while i <= 2189:  # 终止页数

    # file 为文件路径+文件名
    file = 'D:\数据\人民网\第二阶段\人民网getIndex' + str(i) + '.json'
    fp = open(file=file, mode='w', encoding='utf-8')

    # 修改cookie
    cookie = 'WEIBOCN_FROM=1110006030; ' \
             'SUB=_2A25NDrFVDeRhGeFK7FIS9ybIyDmIHXVu8N8drDV6PUJbkdANLWrmkW1NQwr7ATb1kYN21_ABUqFC6FY5gGZlLt7M; ' \
             '_T_WM=61887461574; XSRF-TOKEN=dcb346; MLOGIN=1; ' \
             'M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032286908003%26fid%3D1076032286908003%26uicode' \
             '%3D10000011 '

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',

        'Cookie': cookie
    }

    # 修改url
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2286908003&containerid=1076032286908003&page=' + str(i)
    print(url)
    s = requests.session()
    s.keep_alive = False
    response = s.get(url=url, headers=headers)
    fp.write(response.text)

    # while os.path.getsize(file) < 2048:
    #     print(url)
    #     response = requests.get(url=url, headers=headers)
    #     fp.seek(0)
    #     fp.truncate()
    #     fp.write(response.text)

    time.sleep(3)
    fp.close()
    i += 1
