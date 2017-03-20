
import numpy as np
def test_numpy():
	x2d=np.array(((1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15),(16,17,18)))
	print x2d
	x2d.ravel()
	print x2d
	x2d.resize(3,6)
	print x2d
	x2d.reshape(6,3)
	print x2d
	x2d.shape(9,2)
	print x2d
if __name__ == '__main__':
	test_numpy()