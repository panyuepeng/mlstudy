# coding: utf-8
# Author: pan
# Filename: 

"""

"""


import numpy as np
import scipy
import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
# cfd.plot()


genre_word = [(genre,word) for genre in ['news','romance']
              for word in brown.words(categories=genre)]
print len(genre_word)





if __name__ == '__main__':
    pass