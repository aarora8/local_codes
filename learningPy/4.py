#!/usr/bin/env python

import argparse
import os
import sys
import numpy as np
from scipy import misc
import xml.dom.minidom as minidom

### main ###
dataset_path = os.path.join('/Users/ashisharora/Desktop/summer/hcr data',
                            'largeWriterIndependentTextLineRecognitionTask',
                            'testset.txt')

text_file_path = os.path.join('/Users/ashisharora/Desktop/summer/hcr data',
                               'ascii','lines.txt')

corpus_path = os.path.join('/Users/ashisharora/Desktop/summer/hcr data/corpus','lob.txt')
text_dict = {}
def process_text_file_for_word_model():
  with open(text_file_path, 'rt') as in_file:
    for line in in_file:
      if line[0]=='#':
        continue
      line = line.strip()
      line_vect = line.split(' ')
      text_vect = line.split(' ')[8:]
      text = "".join(text_vect)
      text = text.replace("|", " ")
      text_dict[line_vect[0]] = text

print 'processing word model'
process_text_file_for_word_model()

content = ''
with open(corpus_path) as f:
  for line in f:
    line = line.strip()
    content = content + " " + line

def find_line_in_corpus_file():
  global content
  with open(dataset_path) as f:
    for line in f:
      line = line.strip()
      text = text_dict[line]
      loc = content.find(text)
      print loc
      print text
      # content = content[loc:]

  print 'done function'


print 'finding line in corpus file'
find_line_in_corpus_file()

lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")
for line in open(infilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

# content = ''
# with open(corpus_path) as f:
#   for line in f:
#     line = line.strip()
#     line_vect = line.split(' ')
#     line_text = line_vect[1:]
#     line_text = " ".join(line_text)
#     content = content + " " + line_text
#     print content
#line_to_search_vect = content.split(text)
#print 'done function'
#print line_to_search_vect