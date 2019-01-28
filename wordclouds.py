# This Code from Internet 

import jieba.analyse
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt


def handle(filename, stopword):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    wordlist = jieba.analyse.extract_tags(data, topK=100)   # 分词，取前100
    wordStr = " ".join(wordlist)
    print(wordStr)
    hand = np.array(Image.open('shape.jpg'))    # 打开一张图片，词语以图片形状为背景分布
    my_cloudword = WordCloud(
        # wordcloud参数配置
        width=1024,
        height=768,
        background_color = 'white',   # 背景颜色
        mask = hand,                  # 背景图片
        max_words = 300,              # 最大显示的字数
        stopwords = stopword,         # 停用词
        max_font_size = 100,           # 字体最大值
        font_path='C:\Windows\Fonts\msyh.ttc',  # 设置中文字体，若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        random_state=4,  # 设置有多少种随机生成状态，即有多少种配色方案
    )

    my_cloudword.generate(wordStr)          # 生成图片
    my_cloudword.to_file('wordcloud.png')    # 保存
    plt.imshow(my_cloudword)  # 显示词云图
    plt.axis('off')  # 是否显示x轴、y轴下标
    plt.show()  # 显示


handle('comments.txt', STOPWORDS)
