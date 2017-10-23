#!/usr/bin/env bash

data_dir=data
mkdir -p $data_dir/train/backup
mv $data_dir/train/text.txt $data_dir/train/utt2spk $data_dir/train/images.scp $data_dir/train/backup/
cp $data_dir/train/backup/images.scp $data_dir/train/images.scp
local/augment_and_make_feature_vect.py $data_dir/train 1 --scale-size 40 --max-vertical-shift 10 | \
      copy-feats --compress=true --compression-method=7 \
      ark:- ark,scp:$data_dir/$f/data/images.ark,$data_dir/$f/feats.scp || exit 1

