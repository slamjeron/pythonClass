
def myrange(start,stop=None,step=None):
	lst=[]
	if stop==None:
		stop=start
		start=0
	if step==None:
		step=1
		if start>stop:
			step= -1
	
	if stop>start and step>0:
		while stop>start:
			lst.append(start)
			start+=step
	else:
		if stop<start and step<0:
				while stop<start:
					lst.append(start)
					start+=step
		else:
			return lst
			
	return lst

print('(',10,')')
for i in myrange(10):
	print(i)
print()
print('(',0,10,')')
for i in myrange(0,10):
	print(i)
print()
print('(',0,10,2,')')
for i in myrange(0,10,2):
	print(i)
print()
print('(',10,0,')')
for i in myrange(10,0):
	print(i)
print()
print('(',10,0,3,')')
for i in myrange(10,0,-3):
	print(i)
print()
print('(',0,10,-3,')')
for i in myrange(0,10,-3):
	print(i)
print()
print('(',10,0,3,')')
for i in myrange(10,0,3):
	print(i)
print()
