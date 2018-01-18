import sys
pred_val = open(sys.argv[1], 'r')
pred_sample = open(sys.argv[2], 'r')
pred_submit = open(sys.argv[3], 'w')
class2quant = {}
for line1, line2 in zip(pred_sample, pred_val):
    line1 = line1.strip().split(',')
    sale_date, class_id = line1[0], line1[1]
    sale_quant = float(line2.strip())
    tmp = class2quant.get(class_id, 0)
    tmp += sale_quant
    class2quant[class_id] = tmp
class2quant = sorted(class2quant.items(), key = lambda x:x[0])
for (class_id, sale_quant) in class2quant:
    pred_submit.write('201711,' + class_id + ',' + str(sale_quant) + '\n')
pred_val.close()
pred_sample.close()
pred_submit.close()
