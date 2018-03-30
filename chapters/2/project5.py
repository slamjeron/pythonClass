import sys
def addSpace(str, newLen):
	
	while (len(str)<newLen):
		str+=" "
		
	return str

print(addSpace('date', 8),addSpace('cost', 8),addSpace('cost', 8))