#!/usr/bin/env python

import argparse
import os
import sys
import numpy as np
from scipy import misc

### main ###

test_data = '/Users/ashisharora/Desktop/data/test_text.txt'
corpus_word_count = '/Users/ashisharora/Desktop/data/wl_check'
test_word_count = '/Users/ashisharora/Desktop/data/test_wc.txt'

corpus_dict = {}
with open(corpus_word_count) as f:
  for line in f:
    line = line.strip()
    line_vect = line.split(" ")
    word = line_vect[-1]
    corpus_dict[word] = word

test_dict = {}
count = 0
total_count = 0
with open(test_word_count) as f:
  for line in f:
    line = line.strip()
    line_vect = line.split(" ")
    word = line_vect[-1]
    total_count = total_count + int(line_vect[0])
    if word in corpus_dict.keys():
        #print word , line_vect[0]
        continue
    else:
        test_dict[word] = line_vect[0]
        count = count + int(line_vect[0])

print len(test_dict)
print count
print total_count
print 'done, code complete'