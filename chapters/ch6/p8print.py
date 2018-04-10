import time

def printAll(seq,count):#{
    if seq:#{
        print(seq[0])
        print(count)
        count += 1
        printAll(seq[1:],count)
    #}
#}

start_time = time.time()
seq = ['dose', 'this', 'word']
printAll(seq,0)
print('the loop took ',time.time()-start_time)

'''
this code works as expected it prints every element in the 
sequence. there is no hiden cost t
'''
