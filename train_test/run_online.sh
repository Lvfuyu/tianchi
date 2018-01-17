python train.py ../feature/train_feature.txt ../feature/test_feature.txt ../submit/pred_sale_quant.tmp
python gen_submit.py ../submit/pred_sale_quant.tmp ../sample/test_sample.csv ../submit/firstblood.csv
