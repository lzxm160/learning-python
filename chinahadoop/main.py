import random
import datetime
import time

# print random.random()
# print random.uniform(1,9)
# print random.randrange(20)
# print random.randrange(0,99,3)
# print random.choice('ABCDEFG')
# items=[1,2,3,4,5,6,7,8,9]
# random.shuffle(items)
# print items
# print random.sample([1,2,3,4,5,6,7,8,9],5)
# weighted_choices=[('three',3),('two',2),('one',1)]
# population=[var for var,cnt in weighted_choices for i in range(cnt)]
# print random.choice(population)

def next_5digit_int():
	time.sleep(0.123)
	current_time=datetime.datetime.now().time()
	random_no=int(current_time.strftime('%S%f'))
	return random_no/1000
def test():
	for x in range(0,10):
		i=next_5digit_int()
		print i
import numpy as np
def test_numpy():
	x=np.random.random(10)
	print x
	mean=x.mean()
	print mean
	std=x.std()
	print std
	var=x.var()
	print var
import pandas as pd
import datetime
import pandas_datareader.data as web

def test_pandas():
	start=datetime.datetime(2014,10,1)
	end=datetime.datetime(2015,1,31)
	apple=web.get_data_yahoo('AAPL',start,end)
	print (apple.head())
	apple.to_csv('apple-data.csv')
	df=pd.read_csv('apple-data.csv',index_col='Date',parse_dates=True)
	df.head()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def test_draw():
	df=pd.read_csv('apple-data.csv',index_col='Date',parse_dates=True)
	df['H-L']=df.High-df.Low
	df['50MA']=pd.rolling_mean(df['Close'],50)
	df[['Open','High','Low','Close','50MA']].plot()
	plt.show()
def test_3d():
	df=pd.read_csv('apple-data.csv',parse_dates=True)
	print df.head()
	df['H-L']=df.High-df.Low
	df['50MA']=pd.rolling_mean(df['Close'],50)
	threedee=plt.figure().gca(projection='3d')
	threedee.scatter(df.index,df['H-L'],df['Close'])
	threedee.set_xlabel('Index')
	threedee.set_ylabel('H-L')
	threedee.set_zlabel('Close')
	plt.show()
	threedee=plt.figure().gca(projection='3d')
	threedee.scatter(df.index,df['H-L'],df['Volume'])
	threedee.set_xlabel('Index')
	threedee.set_ylabel('H-L')
	threedee.set_zlabel('Volume')
	plt.show()
def test_pandas():
	# ser_obj=pd.Series(range(10,20))
	# print type(ser_obj)
	# print type(ser_obj.values)
	# print type(ser_obj.index)
	# print ser_obj
	# print ser_obj*2
	# print ser_obj>15
	# year_data={2001:17.8,2002:20.1,2003:16.5}
	# ser_obj=pd.Series(year_data)
	# print ser_obj.head()
	# print ser_obj.index
	array=np.random.randn(5,4)
	df_obj=pd.DataFrame(array)
	print df_obj.head()
if __name__ == '__main__':
	test_pandas()