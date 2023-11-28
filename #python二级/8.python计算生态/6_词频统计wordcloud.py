from jieba import *
from wordcloud import WordCloud
from imageio import imread


def getTxt():
    txt = open("The Way of All Flesh.txt", "r", encoding='GBK').read()
    txt = txt.lower()
    for ch in '!"#%&()*+,.-/:;<=>?@[\\]^_\'{|}~”’“':
        txt = txt.replace(ch, ' ')
    return txt


def changeTxt(txt):
    words = lcut(txt)
    newtxt = ''.join(words)
    return newtxt


def cloudWord(newtxt):
    mask = imread('test_1.png')
    wordcloud = WordCloud(
        background_color='white',
        width=800,
        height=600,
        max_words=200,
        max_font_size=80,
        mask=mask
    ).generate(newtxt)
    wordcloud.to_file('词云_1.png')


def main():
    txt = getTxt()
    newtxt = changeTxt(txt)
    cloudWord(newtxt)


main()
