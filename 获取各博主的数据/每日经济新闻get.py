import requests
import time

i = 2600  # 起始页数

while i <= 5150:  # 终止页数
    file = 'D:\数据\每日经济新闻\每日经济新闻getIndex' + str(i) + '.json'  # 输出路径
    fp = open(file=file, mode='w', encoding='utf-8')

    cookie = 'WEIBOCN_FROM=1110006030; ' \
             'SUB=_2A25ND5AODeRhGeFK7FIS9ybIyDmIHXVu8zBGrDV6PUJbkdANLXD1kW1NQwr7ARAHK8Ivs4aKVI1qowJb1ixA1bVY; ' \
             '_T_WM=87515853294; MLOGIN=1; XSRF-TOKEN=711010; ' \
             'M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E6%25AF%258F%25E6%2597%25A5' \
             '%25E7%25BB%258F%25E6%25B5%258E%25E6%2596%25B0%25E9%2597%25BB%26fid%3D1076031649173367%26uicode' \
             '%3D10000011 '

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',
        'Cookie': cookie
    }

    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1649173367&containerid=1076031649173367&page=' + str(i)
    print(url)
    s = requests.session()
    s.keep_alive = False
    response = s.get(url=url, headers=headers)  # 模拟浏览器发起请求
    fp.write(response.text)  # 写到输出文件里

    time.sleep(3)
    fp.close()
    i += 1
