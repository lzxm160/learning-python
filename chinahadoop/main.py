import random
import datetime
import time

print random.random()
print random.uniform(1,9)
print random.randrange(20)
print random.randrange(0,99,3)
print random.choice('ABCDEFG')
items=[1,2,3,4,5,6,7,8,9]
random.shuffle(items)
print items
print random.sample([1,2,3,4,5,6,7,8,9],5)
weighted_choices=[('three',3),('two',2),('one',1)]
population=[var for var,cnt in weighted_choices for i in range(cnt)]
print random.choice(population)

def next_5digit_int():
	time.sleep(0.123)
	current_time=datetime.datetime.now().time()
	random_no=int(current_time.strftime('%S%f'))
	return random_no/1000
if __name__ == '__main__':
	for x in range(0,10):
		i=next_5digit_int()
		print i