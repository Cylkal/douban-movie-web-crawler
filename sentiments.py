import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt


def snowanalysis(comment):
    sentimentslist = []
    sum = 0
    for li in comment:
        s = SnowNLP(li)
        print(li)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)
        sum += s.sentiments
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01))
    plt.title("Average:"+str(round(sum/len(sentimentslist), 2)))
    plt.show()


comment = []
with open('comments.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if row not in comment:
            comment.append(row.strip('\n'))


snowanalysis(comment)
