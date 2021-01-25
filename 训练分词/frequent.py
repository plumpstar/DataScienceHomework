import jieba

path_txt = 'D:\数据\第一阶段文本.txt'
f = open(path_txt, 'r', encoding='UTF-8').read()

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
cut_text = " ".join(jieba.cut(f))
# print(cut_text)
speech = cut_text.split()
dic = {}
for word in speech:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word] + 1
