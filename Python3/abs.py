def my_abs(x):

	if x>=0:
		return x
	else:
		return -x

m=input('please input your number:')
n=float(m)
if not isinstance(n,(int,float)):
	raise TypeError('your input is so stupid')
print(my_abs(n))
