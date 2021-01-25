import os
import requests
import time
i = 722  # 起始页数

while i <= 750:  # 终止页数

    # file 为文件路径+文件名
    file = 'D:\数据\南方都市报\南方都市报getIndex' + str(i) + '.json'
    fp = open(file=file, mode='w', encoding='utf-8')

    # 修改cookie
    cookie = 'WEIBOCN_FROM=1110006030; loginScene=102003; ' \
             'SUB=_2A25ND5AODeRhGeFK7FIS9ybIyDmIHXVu8zBGrDV6PUJbkdANLXD1kW1NQwr7ARAHK8Ivs4aKVI1qowJb1ixA1bVY; ' \
             '_T_WM=87515853294; XSRF-TOKEN=593f2c; MLOGIN=1; ' \
             'M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231093_-_selffollowed%26fid%3D1076031644489953%26uicode' \
             '%3D10000011 '

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',

        'Cookie': cookie
    }

    # 修改url
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1644489953&containerid=1076031644489953&page=' + str(i)
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

    time.sleep(5)
    fp.close()
    i += 1
