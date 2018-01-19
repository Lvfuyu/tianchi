python train.py ../feature/local_train_feature.txt ../feature/local_test_feature.txt ../submit/local_pred_sale_quant.tmp
python eval.py ../submit/local_pred_sale_quant.tmp ../sample/local_test_sample.csv

#python train.py ../feature/local_train_feature.txt ../feature/local_test_feature.201709.txt ../submit/local_pred_sale_quant.test.tmp
#python gen_submit.py ../submit/local_pred_sale_quant.test.tmp ../sample/local_test_sample.201709.csv ../submit/pred_quant.201710.csv
