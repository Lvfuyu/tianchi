import sys
import math
f_1 = open('result_201709_quant.csv', 'r')
f_2 = open('result_oct_quant.201710.csv', 'r')
err_sum = 0
for line1, line2 in zip(f_1, f_2):
    _, _, sale1 = line1.strip().split(',')
    _, _, sale2 = line2.strip().split(',')
    sale1 = float(sale1)
    sale2 = float(sale2)
    err_sum += (sale1-sale2)*(sale1-sale2)

print math.sqrt(err_sum*1.0/140)
f_1.close()
f_2.close()
