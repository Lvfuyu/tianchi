#!/usr/bin/env python
#_*_coding:utf-8_*_

import numpy as np
import sys
import csv
import sys

def calculate(pdata, psample, pres):
	fdata = open(pdata, 'rb')
	fdata.readline()
	reader = csv.reader(fdata)
	data_lines = [row for row in reader]
	dic = {}
	for data_line in data_lines:
		sale_date,class_id,sale_quantity,brand_id,compartment,type_id,level_id,department_id,TR,gearbox_type,displacement,if_charging,price_level,price,driven_type_id,fuel_type_id,newenergy_type_id,emission_standards_id,if_MPV_id,if_luxurious_id,power,cylinder_number,engine_torque,car_length,car_width,car_height,total_quality,equipment_quality,rated_passenger,wheelbase,front_track,rear_track = data_line

		data_list = [class_id, brand_id, compartment, type_id, level_id, department_id, TR, gearbox_type, displacement, if_charging, price_level, driven_type_id, fuel_type_id, newenergy_type_id, emission_standards_id, if_MPV_id, if_luxurious_id, str(class_id)+'#'+str(brand_id), str(class_id)+'#'+str(TR), str(class_id)+'#'+str(gearbox_type), str(class_id)+'#'+str(displacement), str(class_id)+'#'+str(if_charging), sale_quantity]

		if sale_date not in dic:
			dic[sale_date] = []
		dic[sale_date].append(data_list)

	fres = open(pres, 'w')
	fsample = open(psample, 'rb')
	reader = csv.reader(fsample)
	sample_lines = [row for row in reader]
	for sample_line in sample_lines:
		sale_date = sample_line[0]
		sample_line = sample_line[1:]
		sale_quantity = sample_line[-1]
		sample_line = sample_line[0:-1]
		sample_line.append(str(sample_line[0])+'#'+str(sample_line[1]))
		sample_line.append(str(sample_line[0])+'#'+str(sample_line[6]))
		sample_line.append(str(sample_line[0])+'#'+str(sample_line[7]))
		sample_line.append(str(sample_line[0])+'#'+str(sample_line[8]))
		sample_line.append(str(sample_line[0])+'#'+str(sample_line[9]))
		sample_line.append(sale_quantity)
		feature = []
		for k in range(len(sample_line)-1):
			key = sample_line[k]
			i = 1
			l = []
			while i<6:
				month = int(sale_date[-2:])
				if month <= i:
					month += 12 - i
					if month <10:
						month = '0' + str(month)
					else:
						month = str(month)
					date = str(int(sale_date[0:4])-1) + month
				else:
					month -= i
					if month <10:
						month = '0' + str(month)
					else:
						month = str(month)
					date = sale_date[0:4] + month
				#l = []
				if date in dic:
					for record in dic[date]:
						if record[k]==key:
							l.append(record[-1])
				if i in [1,3,5]:
					if len(l):
						l_np = np.array(l, dtype=float)
						tmp = [l_np.max(), l_np.min(), l_np.sum(), l_np.mean(), l_np.std(), np.median(l_np)]
					else:
						tmp = [0, 0, 0, 0, 0, 0]
					feature.extend(tmp)
				i += 1
		s = str(sample_line[-1])
		for i in range(len(feature)):
			s += " %d:%s"%(i+1, str(feature[i]))
		s += '\n'
		fres.write(s)
	fres.close()
	fsample.close
	fdata.close()

if __name__=="__main__":
	pdata = "../data/train.csv"
	psample = sys.argv[1]
	pres = sys.argv[2]

	calculate(pdata, psample, pres)
