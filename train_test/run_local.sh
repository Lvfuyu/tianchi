python train.py ../feature/local_train_feature.txt ../feature/local_test_feature.txt ../submit/local_pred_sale_quant.tmp
python eval.py ../submit/local_pred_sale_quant.tmp ../sample/local_test_sample.csv
