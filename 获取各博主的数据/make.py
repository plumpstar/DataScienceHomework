import os
import requests
import time

a = [940]


for i in a:  # 终止页数

    # file 为文件路径+文件名
    file = 'D:\数据\共青团中央\第二阶段\共青团中央getIndex' + str(i) + '.json'
    fp = open(file=file, mode='w', encoding='utf-8')

    # 修改cookie
    cookie = 'WEIBOCN_FROM=1110006030; ' \
             'SUB=_2A25NDvkvDeRhGeFK7FIS9ybIyDmIHXVu8IdnrDV6PUJbkdAKLWn8kW1NQwr7ATcUUOqhGUqpc-UacA6_x0OGodRD; ' \
             '_T_WM=45833621280; MLOGIN=1; XSRF-TOKEN=e8cd2f; ' \
             'M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231093_-_selffollowed%26oid%3D3937348351%26fid' \
             '%3D1076033937348351%26uicode%3D10000011 '

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',

        'Cookie': cookie
    }

    # 修改url
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=3937348351&containerid=1076033937348351&page=' + str(
        i)
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

    time.sleep(1)
    fp.close()
