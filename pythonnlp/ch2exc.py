# coding: utf-8
# Author: pan
# Filename: 

import nltk

print nltk.corpus.gutenberg.fileids()

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print len(emma)

emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print emma.concordance('surprize')


print
print

from nltk.corpus import gutenberg
print gutenberg.fileids()

emma = gutenberg.words('austen-emma.txt')
print emma


for fileid in gutenberg.fileids():
    # 字符长
    num_chars = len(gutenberg.raw(fileid))
    # 单词数量
    num_words = len(gutenberg.words(fileid))
    # 句子数量
    num_sents = len(gutenberg.sents(fileid))
    # 文章中单词数量去重
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_chars / num_words), int(num_words / num_sents), \
        int(num_words / num_vocab), fileid


if __name__ == '__main__':
    pass