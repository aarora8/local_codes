#!/usr/bin/env python

import argparse
import os
import sys
import numpy as np
from scipy import misc

### main ###

input_data = '/Users/ashisharora/Desktop/result.txt'
output_data = '/Users/ashisharora/Desktop/output.txt'
phones_id = '/Users/ashisharora/Desktop/phones.txt'
words_id = '/Users/ashisharora/Desktop/words.txt'

# extracting line by line phoneid and phone
phone_dict = dict()
phone_mapping = open(phones_id, 'r')
phone_data = phone_mapping.read()
phone_data = phone_data.strip()
phone_data_vect = phone_data.split("\n")

# storing phoneid and phone in a dict
for key_val in phone_data_vect:
  key_val = key_val.split(" ")
  key = key_val[1]
  val = key_val[0]
  phone_dict[key] = val

word_dict = dict()
word_mapping = open(words_id, 'r')
word_data = word_mapping.read()
word_data = word_data.strip()
word_data_vect = word_data.split("\n")

# storing wordid and word in a dict
for key_val in word_data_vect:
  key_val = key_val.split(" ")
  key = key_val[1]
  val = key_val[0]
  word_dict[key] = val

# getting utteranceID and word list
# getting utteranceID and phone list
utt_word_dict = dict()
utt_phone_dict = dict()
with open(input_data) as f:
  for line in f:
    line = line.strip()
    line_vect = line.split("\t")
    uttID = line_vect[0]
    word = line_vect[4]
    phones = line_vect[5]
    if uttID in utt_word_dict.keys():
      utt_word_dict[uttID].append(word)
      utt_phone_dict[uttID].append(phones)
    else:
      utt_word_dict[uttID] = list()
      utt_word_dict[uttID].append(word)
      utt_phone_dict[uttID] = list()
      utt_phone_dict[uttID].append(phones)

unk_word_dict = dict()
# for unk getting word from phone
# getting utteranceID and phone list
for key in sorted(utt_word_dict.iterkeys()):
  for index, value in enumerate(utt_word_dict[key]):
    # get phonelistID for unk word
    if value == '231':
      phone_key = utt_phone_dict[key][index]
      phone_val_vect = list()
      phone_key_vect = phone_key.split(" ")
      #get word from phonelistID
      for pkey in phone_key_vect:
        phone_val = phone_dict[pkey]
        phone_val_vect.append(phone_val)
      phone_2_word = list()
      for phone in phone_val_vect:
        phone_2_word.append(phone.split('_')[0])
      phone_2_word = ''.join(phone_2_word)
      #print "%s: %s" % (key, phone_2_word)
      if key in unk_word_dict.keys():
        unk_word_dict[key][index]= phone_2_word
      else:
        unk_word_dict[key] = dict()
        unk_word_dict[key][index] = phone_2_word

for key in sorted(unk_word_dict.iterkeys()):
  for index in sorted(unk_word_dict[key].iterkeys()):
    print "%s: %s" % (key, index)
    print unk_word_dict[key][index]