import random
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