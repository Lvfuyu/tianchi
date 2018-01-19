python train.py ../feature/train_feature.txt ../feature/test_feature.txt ../submit/pred_sale_quant.tmp
python gen_submit.py ../submit/pred_sale_quant.tmp ../sample/test_sample.csv ../submit/submit_to_rename.csv
#python train.py ../feature/local_train_feature.txt ../feature/local_test_feature.txt ../submit/pred_sale_quant.tmp
#python gen_submit.py ../submit/pred_sale_quant.tmp ../sample/test_sample.csv ../submit/submit_to_rename.csv
