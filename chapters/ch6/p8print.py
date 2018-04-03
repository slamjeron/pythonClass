def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])


seq = ['dose', 'this', 'word']

printAll(seq)

'''
this code works as expected it prints every element in the 
sequence.
'''
