#!/usr/bin/env python

import argparse
import os
import sys
import numpy as np
from scipy import misc
import xml.dom.minidom as minidom



### main ###
text_dict = {}
xml_path = os.path.join('/Users/ashisharora/Desktop/summer/hcr data', 'xml')
xml_files = os.listdir(xml_path)
for first_file in xml_files:
  first_path = os.path.join(xml_path, first_file)
  doc = minidom.parse(first_path)
  form_elements = doc.getElementsByTagName('form')[0]
  writer_id = form_elements.getAttribute('writer-id')

  outerfolder = form_elements.getAttribute('id')[0:3]
  innerfolder = form_elements.getAttribute('id')
  line_elements = doc.getElementsByTagName('line')
  image_file_path_list = []
  for ele in line_elements:
    text = ele.getAttribute('text')
    image_id = ele.getAttribute('id')
    img_num = ele.getAttribute('id')[-3:]
    utt_id = writer_id + '_' + image_id
    text_dict[image_id] = text

### main ###
dataset_path = os.path.join('/Users/ashisharora/Desktop/summer/hcr data',
                            'largeWriterIndependentTextLineRecognitionTask',
                            'testset.txt')

text_file_path = os.path.join('/Users/ashisharora/Desktop/summer/hcr data',
                               'ascii','lines.txt')

corpus_path = os.path.join('/Users/ashisharora/Desktop/summer/hcr data/corpus','lob.txt')


content = ''
with open(corpus_path) as f:
  for line in f:
    line = line.strip()
    content = content + " " + line

# with open(corpus_path) as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]

def find_line_in_corpus_file():
  global content
  counter = 0
  with open(dataset_path) as f:
    for line in f:
      line = line.strip()
      text = text_dict[line]
      prev_loc = loc
      loc = content.find(text)
      if loc == -1:
          counter = counter+1
          print text
          print prev_loc
          print line
    print counter
      #print text
      # content = content[loc:]

  print 'done function'


print 'finding line in corpus file'
find_line_in_corpus_file()
