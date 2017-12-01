#!/usr/bin/env bash


dir=exp/chain_fsf5_1/cnn_chainali_1a/decode_test
lattice-scale --inv-acoustic-scale=12 "ark:gunzip -c $dir/lat.1.gz|" ark:- | \
        lattice-1best ark:- ark:- | \
        lattice-align-words data/lang_unk/phones/word_boundary.int exp/chain_fsf5_1/cnn_chainali_1a/final.mdl ark:- ark:- | \
        lattice-arc-post exp/chain_fsf5_1/cnn_chainali_1a/final.mdl ark:- - | \
        local/unk_ark_post_to_transcription.py data/lang_unk/phones.txt data/lang_unk/words.txt

dir=exp/chainpdp/cnn1a_chainali/decode_test_unk
$cmd $dir/scoring_kaldi/penalty_0.5/log/score.12.log \
      cat $dir/scoring_kaldi/penalty_0.5/12.txt \| \
      compute-wer --text --mode=present \
      ark:$dir/scoring_kaldi/test_filt.txt  ark,p:- ">&" $dir/wer_LMWT_0.5


data_dir=data
mkdir -p $data_dir/train/backup
mv $data_dir/train/text.txt $data_dir/train/utt2spk $data_dir/train/images.scp $data_dir/train/backup/
cp $data_dir/train/backup/images.scp $data_dir/train/images_new.scp
augment_and_make_feature_vect.py $data_dir/train 1 --scale-size 40 --vertical-shift 10

dl_dir=data/download
file_name=largeWriterIndependentTextLineRecognitionTask
dataset=trainset.txt
full_path="$dl_dir/$file_name/$dataset"
echo $full_path

lattice-best-path "ark:gunzip -c exp/chain/tri3_train_lats_chain/lat.1.gz |" ark:/dev/null ark:- |
ali-to-phones --write-lengths=true exp/chain/cnn_chainali_1a/final.mdl ark:- ark,t:alignment.txt
