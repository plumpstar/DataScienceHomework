from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import imageio
path_txt = 'D:\数据\第一阶段文本.txt'
f = open(path_txt, 'r', encoding='UTF-8').read()

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
cut_text = " ".join(jieba.cut(f))

with open('E:\Python\HanLP分词\处理第一阶段\stopwords.txt', 'r', encoding='utf-8') as fp:
    # 读取内容
    st_words = fp.readlines()
    # print('st_words:\n', st_words)
    # 剔除 停止词两侧的 空白字符
    st_words = [words.strip() for words in st_words]
    # 剔除重复的 停止词
    st_words = list(set(st_words))
    # print('st_words:\n', st_words)

# print(cut_text)
color_mask = imageio.imread("E:\Python\HanLP分词\wordCLOUD\\20191211143206410.jpg")
wordcloud = WordCloud(
    # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
    font_path="C:/Windows/Fonts/simfang.ttf",
    # 设置了背景，宽高
    background_color="white",
    width=1000,
    height=880,
    stopwords=st_words,
    mask=color_mask
    ).generate(cut_text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
