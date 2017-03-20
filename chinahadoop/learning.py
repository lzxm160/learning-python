
import numpy as np
def test_numpy():
	# x2d=np.array(((1,2,3),(4,5,6),(7,8,9)))
	# print x2d.shape
	# print x2d.dtype
	# print x2d.size
	# print x2d.itemsize
	# print x2d.ndim
	# print x2d.data
	x=np.array([1,2,3,4,5,6,7,8,9])
	print x[3:7]
if __name__ == '__main__':
	test_numpy()