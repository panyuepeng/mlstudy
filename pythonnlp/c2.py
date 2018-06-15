# coding: utf-8
# Author: pan
# Filename: 

"""
就职演说语料库
"""

import numpy as np
import scipy
from nltk.corpus import inaugural
print inaugural.fileids()

print [fileid[:4] for fileid in inaugural.fileids()]

import nltk

cfd = nltk.ConditionalFreqDist((target, fileid[:4]) for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))

# cfd.plot()

print '-----------------'
corpus_root  = u"/media/pan/新加卷/data/"
from nltk.corpus import PlaintextCorpusReader
wordlists = PlaintextCorpusReader(corpus_root, ".*")
print wordlists.fileids()
print wordlists.words('data.300m')



if __name__ == '__main__':
    pass
