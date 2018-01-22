#-*-coding:utf-8 -*-

a = input('please input your weight(kg):')
b = input('please input your higher(m):')
weight = float(a)
higher = float(b)
bmi = weight/(higher*higher)
if bmi<=18.5:
	print('your bmi is',bmi)
	print('you are too slim.')
elif bmi<=25 and bmi>18.5:
	print('your bmi is',bmi)
	print('your weight is common')
elif bmi>25 and bmi<=28:
	print('you are overweight,hiahiahia!!!')
	print('your bmi is :',bmi)
elif bmi>28 and bmi<=32:
	print('you are so fat')
	print('your bmi is :',bmi)
elif bmi>32:
	print('your bmi is:',bmi)
	print('too fat')