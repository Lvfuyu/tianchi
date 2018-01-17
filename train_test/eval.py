import sys
import math
pred_val = open(sys.argv[1], 'r')
pred_sample = open(sys.argv[2], 'r')
class2quant_pred = {}
class2quant_true = {}

for line1, line2 in zip(pred_sample, pred_val):
    line1 = line1.strip().split(',')
    sale_date, class_id, true_sale_quant = line1[0], line1[1], float(line1[-1])
    sale_quant = float(line2.strip())
    tmp = class2quant_pred.get(class_id, 0)
    tmp += sale_quant
    class2quant_pred[class_id] = tmp
    
    _tmp = class2quant_true.get(class_id, 0)
    _tmp += true_sale_quant
    class2quant_true[class_id] = _tmp

err_sqr_sum = 0
for (class_id, true_sale_quant) in class2quant_true.items():
    err_sqr_sum += (true_sale_quant - class2quant_pred[class_id])*(true_sale_quant - class2quant_pred[class_id])
print 'TEST RMSE = ' + str(math.sqrt(err_sqr_sum*1.0/len(class2quant_true)))
pred_val.close()
pred_sample.close()
