four = {
    '第四阶段 (1)': '3月10日',
    '第四阶段 (2)': '3月11日',
    '第四阶段 (3)': '3月12日',
    '第四阶段 (4)': '3月13日',
    '第四阶段 (5)': '3月14日',
    '第四阶段 (6)': '3月15日',
    '第四阶段 (7)': '3月16日',
    '第四阶段 (8)': '3月17日',
    '第四阶段 (9)': '3月18日',
    '第四阶段 (10)': '3月19日',
    '第四阶段 (11)': '3月20日',
    '第四阶段 (12)': '3月21日',
    '第四阶段 (13)': '3月22日',
    '第四阶段 (14)': '3月23日',
    '第四阶段 (15)': '3月24日',
    '第四阶段 (16)': '3月25日',
    '第四阶段 (17)': '3月26日',
    '第四阶段 (18)': '3月27日',
    '第四阶段 (19)': '3月28日',
    '第四阶段 (20)': '3月29日',
    '第四阶段 (21)': '3月30日',
    '第四阶段 (22)': '3月31日',
    '第四阶段 (23)': '4月1日',
    '第四阶段 (24)': '4月2日',
    '第四阶段 (25)': '4月3日',
    '第四阶段 (26)': '4月4日',
    '第四阶段 (27)': '4月5日',
    '第四阶段 (28)': '4月6日',
    '第四阶段 (29)': '4月7日',
    '第四阶段 (30)': '4月8日',
    '第四阶段 (31)': '4月9日',
    '第四阶段 (32)': '4月10日',
    '第四阶段 (33)': '4月11日',
    '第四阶段 (34)': '4月12日',
    '第四阶段 (35)': '4月13日',
    '第四阶段 (36)': '4月14日',
    '第四阶段 (37)': '4月15日',
    '第四阶段 (38)': '4月16日',
    '第四阶段 (39)': '4月17日',
    '第四阶段 (40)': '4月18日',
    '第四阶段 (41)': '4月19日',
    '第四阶段 (42)': '4月20日',
    '第四阶段 (43)': '4月21日',
    '第四阶段 (44)': '4月22日',
    '第四阶段 (45)': '4月23日',
    '第四阶段 (46)': '4月24日',
    '第四阶段 (47)': '4月25日',
    '第四阶段 (48)': '4月26日',
    '第四阶段 (49)': '4月27日',
    '第四阶段 (50)': '4月28日',
    '第四阶段 (51)': '4月29日',
    '第四阶段 (52)': '4月30日',
    '第四阶段 (53)': '5月1日',
    '第四阶段 (54)': '5月2日',
    '第四阶段 (55)': '5月3日',
    '第四阶段 (56)': '5月4日',
    '第四阶段 (57)': '5月5日',
    '第四阶段 (58)': '5月6日',
    '第四阶段 (59)': '5月7日',
    '第四阶段 (60)': '5月8日',
    '第四阶段 (61)': '5月9日',
    '第四阶段 (62)': '5月10日',
    '第四阶段 (63)': '5月11日',
    '第四阶段 (64)': '5月12日',
    '第四阶段 (65)': '5月13日',
    '第四阶段 (66)': '5月14日',
    '第四阶段 (67)': '5月15日',
    '第四阶段 (68)': '5月16日',
    '第四阶段 (69)': '5月17日',
    '第四阶段 (70)': '5月18日',
    '第四阶段 (71)': '5月19日',
    '第四阶段 (72)': '5月20日',
    '第四阶段 (73)': '5月21日',
    '第四阶段 (74)': '5月22日',
    '第四阶段 (75)': '5月23日',
    '第四阶段 (76)': '5月24日',
    '第四阶段 (77)': '5月25日',
    '第四阶段 (78)': '5月26日',
    '第四阶段 (79)': '5月27日',
    '第四阶段 (80)': '5月28日',
    '第四阶段 (81)': '5月29日',
    '第四阶段 (82)': '5月30日',
    '第四阶段 (83)': '5月31日',
    '第四阶段 (84)': '6月1日',
    '第四阶段 (85)': '6月2日',
    '第四阶段 (86)': '6月3日',
    '第四阶段 (87)': '6月4日',
    '第四阶段 (88)': '6月5日',
    '第四阶段 (89)': '6月6日',
    '第四阶段 (90)': '6月7日',
    '第四阶段 (91)': '6月8日',
    '第四阶段 (92)': '6月9日',
    '第四阶段 (93)': '6月10日',
}

i = 1
while i <= 93:
    print(i)
    filename = 'D:\汇总\第四阶段\第四阶段' + ' (' + str(i) + ').csv'
    f = open(file=filename, mode='r', encoding='utf-8')
    output = 'D:\数据\筛选\第四阶段\\' + four.get('第四阶段' + ' (' + str(i) + ')') + '.csv'
    fp = open(file=output, mode='a+', encoding='utf-8')
    for line in f:
        if int(line.strip().split(',')[1]) > 80:
            fp.write(line)
    fp.close()
    f.close()
    i += 1
