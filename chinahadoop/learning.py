
import numpy as np
def test_numpy():
	x2d=np.array(((1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15),(16,17,18)))
	print x2d
	print '-----------------'
	x2d.ravel()
	print x2d
	print '-----------------'
	x2d.resize(3,6)
	print x2d
	print '-----------------'
	x2d.reshape(6,3)
	print x2d
	print '-----------------'
	x2d.shape=(9,2)
	print x2d
def test_numpy2():
	a=np.matrix('1 2 3;4 5 6;7 8 9')
	print a
	b=np.matrix('4 5 6;7 8 9;10 11 12')
	print b
	print a*b
def test_numpy3():
	import numpy.ma as ma
	x=np.array([72,79,85,90,150,-135,120,-10,60,100])
	mx=ma.mask_array(x,mask=[0,0,0,0,0,1,0,1,0,0])
	mx2=ma.mask_array(x,mask=x<0)
	print x.mean()
	print mx.mean()
	print mx2.mean()
if __name__ == '__main__':
	# test_numpy()
	# test_numpy2()
	test_numpy3()