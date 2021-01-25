import os
import requests
import time
i = 2587  # 起始页数

while i <= 2865:  # 终止页数

    # file 为文件路径+文件名
    file = 'D:\数据\头条新闻\第一阶段\头条新闻getIndex' + str(i) + '.json'
    fp = open(file=file, mode='w', encoding='utf-8')

    # 修改cookie
    cookie = 'WEIBOCN_FROM=1110006030; ' \
             'SUB=_2A25NDRtSDeRhGeFK7FIS9ybIyDmIHXVu8aUarDV6PUJbkdAKLVrdkW1NQwr7AVUlxXuCqeKJUn4hSqMc_LpiVG5b; ' \
             '_T_WM=60525188506; MLOGIN=1; XSRF-TOKEN=0351ae; ' \
             'M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231093_-_selffollowed%26fid%3D1005051618051664%26uicode' \
             '%3D10000011 '

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',

        'Cookie': cookie
    }

    # 修改url
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1618051664&containerid=1076031618051664&page=' + str(i)
    print(url)
    response = requests.get(url=url, headers=headers)
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
