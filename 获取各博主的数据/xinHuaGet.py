import os
import requests
import time
i = 640  # 起始页数

while i <= 816:  # 终止页数

    # file 为文件路径+文件名
    file = 'D:\数据\新华网\第四阶段\新华网getIndex' + str(i) + '.json'
    fp = open(file=file, mode='w', encoding='utf-8')

    # 修改cookie
    cookie = 'WEIBOCN_FROM=1110006030; ' \
             'SUB=_2A25NDsTcDeRhGeFK7FIS9ybIyDmIHXVu8OyUrDV6PUJbkdAKLUr7kW1NQwr7AX2ObFPXqDlHC5_LhDW6BJbKbAYK; ' \
             '_T_WM=10752012001; MLOGIN=1; XSRF-TOKEN=de6e74; ' \
             'M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231093_-_selffollowed%26fid%3D1005052810373291%26uicode' \
             '%3D10000011 '

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',

        'Cookie': cookie
    }

    # 修改url
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2810373291&containerid=1076032810373291&page=' + str(i)
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
    i += 1
